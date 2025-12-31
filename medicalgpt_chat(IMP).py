print("MedicalGPT starting...\nType 'exit' or 'quit' to stop.\n")

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader("data/anatomy_phys_vol2.pdf")
pages = loader.load()

# Chunk text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(pages)

# Use a small subset for context (for speed + stability)
context_docs = chunks[:8]
context = "\n\n".join(doc.page_content for doc in context_docs)

# LLM
llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)

# Chat loop
while True:
    user_question = input("\nYou: ")

    if user_question.lower() in ["exit", "quit"]:
        print("\nMedicalGPT: Goodbye!")
        break

    prompt = (
        "You are a medical assistant.\n\n"
        "Answer the question strictly using the context below.\n"
        "If the answer is not present in the context, say "
        "\"I don't know based on the provided document.\"\n\n"
        "Context:\n"
        f"{context}\n\n"
        "Question:\n"
        f"{user_question}\n\n"
        "Important:\n"
        "- Do NOT provide diagnosis\n"
        "- Do NOT prescribe medication\n"
        "- This is for educational purposes only\n"
    )

    response = llm.invoke(prompt)

    print("\nMedicalGPT:", response.content)
