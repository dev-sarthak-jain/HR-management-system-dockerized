from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage
import os
from dotenv import load_dotenv
load_dotenv(override=True)




def initialize_openai_model():
    # Initialize the OpenAI model with your API key
    # Here, we use the `OpenAI` class from Langchain
    api_key=os.getenv("OPENAI_API_KEY")
    return OpenAI(openai_api_key=api_key)

def generate_response(user_input, past_convo):
    # Construct a conversation chain with the model, prompt, and memory
    model = initialize_openai_model()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                "You are a AI assistant on an HR management system. You will answer queries related to a HR management and related queries and try to extend these boundries as much as possible. You will not answer completely random problems completely out of the context of your role."
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )

    # Create an LLM chain with the model, prompt, and memory
    conversation = LLMChain(llm=model, prompt=prompt, memory=memory)

    # Update memory with past conversation
    for exchange in past_convo:
        memory.save_context({"input": exchange["user"]}, {"output": exchange["AI"]})

    # Run the conversation chain
    # response = conversation({"question": user_input})
    try:
        response = conversation.invoke({"question": user_input})
    except Exception as e:
        print(f"Error during conversation execution: {e}")
        return None


    # Extract only the AI's response from the 'text' field
    # print(response, type(response))
    ai_response = response['text'].split('\n')[-1]

    # If the response contains the "AI:" prefix, remove it
    if ai_response.startswith("AI: System: "):
        ai_response = ai_response[12:]

    return ai_response