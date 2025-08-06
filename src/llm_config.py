from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def load_llm(model_id="llama3-70b-8192", temperature=0.7):
    return ChatGroq(
        model=model_id,
        temperature=temperature,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
