from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

DB_DIR = "yelp_chroma_db"

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

vector_store = Chroma(
    collection_name="yelp_reviews",
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

retriever = vector_store.as_retriever(search_kwargs={"k": 8})

model = OllamaLLM(model="llama3.2")

prompt = ChatPromptTemplate.from_template("""
You analyze real customer restaurant reviews.

REVIEWS:
{reviews}

QUESTION:
{question}

RULES:
- Use only the reviews provided.
- No guessing or hallucinating.
- If reviews are insufficient, say: "Not enough review data."

ANSWER:
""")

while True:
    q = input("\nAsk something (q to quit): ")

    if q.lower() == "q":
        break

    docs = retriever.invoke(q)
    joined = "\n".join(d.page_content for d in docs)

    response = (prompt | model).invoke({
        "reviews": joined,
        "question": q
    })

    print("\nANSWER:\n", response)
