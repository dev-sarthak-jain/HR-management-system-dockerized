from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
import os
from dotenv import load_dotenv
load_dotenv(override=True)

def initialize_openai_model():
    # Initialize the OpenAI model with your API key
    # openai_api_key = os.getenv("OPENAI_API_KEY")  # Ensure this matches your .env file
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return OpenAI(openai_api_key=openai_api_key)

def generate_chat_title(question):
    model = initialize_openai_model()

    prompt_text = f"Given the question: '{question}', generate a concise, engaging chat title of 5-6 words."

    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(prompt_text),
        ]
    )

    title_generation_chain = LLMChain(llm=model, prompt=prompt)

    try:
        response = title_generation_chain.invoke({})
        title = response['text'].strip()
        title = title.strip('"')

        return title
    except Exception as e:
        print(f"Error in generating chat title: {e}")
        return "Error: Unable to generate chat title"



'''
if __name__ == "__main__":
    initial_question = "how many people are working in the organization right now?"
    chat_title = generate_chat_title(initial_question)
    print(f"Generated Chat Title: {chat_title}")
'''