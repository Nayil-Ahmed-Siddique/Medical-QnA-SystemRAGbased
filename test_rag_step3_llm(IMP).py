print("STEP 3 START")

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader("data/anatomy_phys_vol2.pdf")
pages = loader.load()

print("Pages loaded:", len(pages))

# Chunk text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(pages)
print("Chunks created:", len(chunks))

# Use small subset as context
context_docs = chunks[:5]
context = "\n\n".join(doc.page_content for doc in context_docs)

# LLM
llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)

prompt = (
    "You are a medical assistant.\n\n"
    "Answer the question using ONLY the context below.\n"
    "If the answer is not in the context, say "
    "\"I don't know based on the provided document.\"\n\n"
    "Context:\n"
    f"{context}\n\n"
    "Question:\n"
    "What is anatomy?\n"
)

print("Calling LLM...")

response = llm.invoke(prompt)

print("\n--- ANSWER ---\n")
print(response.content)

print("STEP 3 END")
