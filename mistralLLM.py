from langchain_mistralai import ChatMistralAI
import dotenv
import os

dotenv.load_dotenv()




llm = ChatMistralAI(
    api_key=os.getenv("API_KEY"),
    
)


print (llm.invoke("Hello, how are you?"))