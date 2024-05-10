import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase

load_dotenv(override=True)
API_KEY = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = API_KEY
# Define the database URI
db_uri = 'mysql://root:abcd1234@localhost:3306/HR_management_system'
  #Adjust the path as necessary
db = SQLDatabase.from_uri(db_uri)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
chain = create_sql_query_chain(llm, db)
answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.
    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: """
)
# Load environment variables from .env file

def generate_response(question):

    query = chain.invoke({"question": question})
    result = db.run(query)
    print(query)
    # Define a runnable chain to process user questions
    runnable_chain = (
        RunnablePassthrough()
        | answer_prompt
        | llm
        | StrOutputParser()
    )

    # Invoke the chain with the user question
    response = runnable_chain.invoke({"question" : question, "query":query, "result" : result})

    return response



def main():
    user_question = 'How many employees are there?'
    answer = generate_response(user_question)
    print(answer)

if __name__ == "__main__":
    main()