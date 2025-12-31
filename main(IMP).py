from langchain_openai import ChatOpenAI

print("Testing LLM connectivity...")

llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)

response = llm.invoke("Explain what anatomy is in one sentence.")

print("\nLLM Response:")
print(response.content)
