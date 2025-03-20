from langchain_mistralai.chat_models import ChatMistralAI
from langchain_mistralai.embeddings import MistralAIEmbeddings
# from langchain_community.chat_models import ChatMistralAI
import dotenv
# import getpass
import os

dotenv.load_dotenv()
# if "MISTRAL_API_KEY" not in os.environ:
#     os.environ["MISTRAL_API_KEY"] = getpass.getpass("Enter your Mistral API key: ")


llm = ChatMistralAI()


print(llm.invoke(input()).content)