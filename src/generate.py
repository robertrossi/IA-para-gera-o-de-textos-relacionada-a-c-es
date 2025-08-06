from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

def llm_generate(llm, user_prompt):
    with open("prompts/base_prompt.txt", "r", encoding="utf-8") as file:
        system_prompt = file.read().strip()

    template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{prompt}"),
    ])

    chain = template | llm | StrOutputParser()

    return chain.invoke({"prompt": user_prompt})
