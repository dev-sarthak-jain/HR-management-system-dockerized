import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase

# Load environment variables from .env file
load_dotenv(override=True)
API_KEY = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = API_KEY
db_uri = 'sqlite:///backend/db.sqlite3'  # Adjust the path as necessary
db = SQLDatabase.from_uri(db_uri)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def answer_question(question):
    # Create the SQL query chain
    chain = create_sql_query_chain(llm, db)

    # Define a prompt template for answering user questions
    answer_prompt = PromptTemplate.from_template(
        """Given the following user question, corresponding SQL query, and SQL result, answer the user question.
        Question: {question}
        SQL Query: {query}
        SQL Result: {result}
        Answer: """
    )

    # Define a runnable chain to process user questions
    runnable_chain = (
        RunnablePassthrough()
        .assign(query=lambda data: data['question'])  # Pass user question as SQL query
        .assign(result=lambda data: db.run(data['query']))  # Execute SQL query and get result
        | answer_prompt  # Use prompt template to generate response
        | llm  # Pass response to ChatOpenAI model
        | StrOutputParser()  # Parse output from ChatOpenAI model
    )

    # Invoke the chain with the user question
    response = runnable_chain.invoke({"question": question})

    return response

# Example usage
user_question = 'How many employees are there?'
answer = answer_question(user_question)
print(answer)
