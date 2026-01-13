# vector_resume.py  — continue indexing FROM last point

import time
import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

CSV_FILE = "restaurant_reviews_clean.csv"
DB_DIR = "yelp_chroma_db"

RESUME_AT = 23000      # last successfully indexed count

print("Loading dataset...")
df = pd.read_csv(CSV_FILE)

print(f"Total reviews: {len(df)}")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

vector_store = Chroma(
    collection_name="yelp_reviews",
    persist_directory=DB_DIR,
    embedding_function=embeddings,
)

docs = []

for _, row in df.iterrows():
    text = str(row["review_text"])
    if len(text) > 1200:
        text = text[:1200]

    docs.append(
        Document(
            page_content=text,
            metadata={
                "restaurant": row["restaurant"],
                "city": row["city"],
                "state": row["state"],
                "business_rating": row["business_rating"],
                "review_rating": row["review_rating"],
                "address": row.get("address"),
                "latitude": row.get("latitude"),
                "longitude": row.get("longitude"),
                "price": row.get("price"),
                "cuisine": row.get("cuisine"),
            },
        )
    )

BATCH = 100
total = len(docs)

print(f"Resuming at {RESUME_AT} of {total}…")

for i in range(RESUME_AT, total, BATCH):
    batch = docs[i : i + BATCH]

    for attempt in range(4):
        try:
            vector_store.add_documents(batch)
            print(f"Indexed {i + len(batch)} / {total}")
            break
        except Exception as e:
            print(f"⚠️ Batch {i} failed ({e}). Retrying in 6s…")
            time.sleep(6)

print("\n🎯 Indexing completed successfully!")
