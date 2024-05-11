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
API_KEY = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = API_KEY
db_uri = 'mysql://root:abcd1234@localhost:3306/HR_management_system'
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