import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase

from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage

#initializtion
load_dotenv(override=True)

db_name = os.environ.get('DATABASE_NAME')
db_user = os.environ.get('DATABASE_USER')
db_password = os.environ.get('DATABASE_PASSWORD')
db_host = os.environ.get('DATABASE_HOST')
db_port = os.environ.get('DATABASE_PORT')
db_uri = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
openai_api_key = os.environ.get('OPENAI_API_KEY')  # Corrected the environment variable name

print(openai_api_key)

#db_uri = 'postgresql://postgres:abcd1234@localhost:5432/HR_management_system'
#db_uri = 'mysql://root:abcd1234@localhost:3306/HR_management_system'
#db_uri = 'sqlite:///mydatabase.db'

openai_api_key = str(openai_api_key)
os.environ['OPENAI_API_KEY'] = openai_api_key



db = SQLDatabase.from_uri(db_uri)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
chain = create_sql_query_chain(llm, db)


answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, SQL result, and previous chat history, answer the user question. If you analyze the question and the answer is not that of a SQL query then answer in general using regular LLM functionalities. 
    Previous Chat History: {chat_history}
    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: """
)
def generate_response(question, past_convo):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    for exchange in past_convo:
        memory.save_context({"input": exchange["user"]}, {"output": exchange["AI"]})
    query = chain.invoke({"question": question})
    result = db.run(query)
    print(query)
    runnable_chain = (
        RunnablePassthrough()
        | answer_prompt
        | llm
        | StrOutputParser()
    )
    response = runnable_chain.invoke({"question" : question, "query":query, "result" : result, "chat_history": memory})

    return response



def main():
    user_question = 'How many employees are there?'
    answer = generate_response(user_question)
    print(answer)

if __name__ == "__main__":
    main()