from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)

def summarize_text(text):

    prompt = PromptTemplate(
        template="""
        {instruction}

        Text:
        {text}

        Summary:
        """,
        input_variables=["text"],
        partial_variables={
            "instruction":
            "Summarize the following text in 5 bullet points."
        }
    )

    chain = prompt | llm

    response = chain.invoke({
        "text": text
    })

    return response.content