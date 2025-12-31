print("STEP 1 START")

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    base_url="https://openrouter.ai/api/v1"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

print("Vector store loaded successfully")
print("STEP 1 END")
