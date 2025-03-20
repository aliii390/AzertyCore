from langchain_mistralai import ChatMistralAI
import os





llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
    max_retries=2,
    # other params...
)


print llm.invoke("Hello, how are you?")