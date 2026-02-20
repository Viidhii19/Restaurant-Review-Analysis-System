# 🍽 Restaurant Review Analysis System

An AI-powered Restaurant Intelligence Platform that analyzes thousands of real customer reviews using Retrieval-Augmented Generation (RAG) to provide accurate, evidence-based insights about restaurants — not hallucinated answers.

This system allows users to ask natural-language questions about restaurants and receive answers grounded in real customer experiences.
# 🚀 What This Project Does

Instead of manually reading hundreds of Google/Yelp reviews, this system lets users ask questions like:
“Is this restaurant good for business meetings?”
“Is the food overpriced?”
“How is the service speed?”
“Which dishes are praised the most?”
“What are the common complaints?”

The AI then answers using only real reviews stored in the vector database.

# 🧠 Core Technology

This project uses a RAG (Retrieval-Augmented Generation) architecture, which means:

The LLM does not guess.
It first retrieves real reviews → then generates answers from those reviews.

# Architecture
                        ┌────────────────────────┐
                        │     Yelp Open Dataset   │
                        │ (Business + Reviews)    │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │   Data Preprocessing    │
                        │   (process_yelp.py)     │
                        │  - Filters restaurants │
                        │  - Cleans review text   │
                        │  - Links business info  │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │  Cleaned CSV Dataset    │
                        │ restaurant_reviews_    │
                        │        clean.csv        │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │   Embedding Engine      │
                        │   (Ollama - mxbai)      │
                        │ Converts text → vectors│
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │   Vector Database       │
                        │     (ChromaDB)          │
                        │ Stores embeddings +    │
                        │ metadata               │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │   Retriever Engine     │
                        │  (Semantic Search)     │
                        │ Fetches relevant       │
                        │ reviews by meaning     │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │     Skill Router        │
                        │ Detects intent:         │
                        │ Food / Service / Price  │
                        │ Ambience / Trends etc.  │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │  Large Language Model   │
                        │     (LLaMA 3.2)         │
                        │ Summarizes & reasons    │
                        │ ONLY using retrieved   │
                        │ reviews                │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │     Streamlit UI        │
                        │ - Restaurant selector  │
                        │ - Cuisine filter       │
                        │ - Ratings              │
                        │ - Natural language Q&A │
                        │ - Review transparency  │
                        └────────────────────────┘
# 📦 Tech Stack
| Layer         | Technology                 |
| ------------- | -------------------------- |
| Language      | Python                     |
| LLM           | LLaMA 3.2 (Ollama)         |
| Embeddings    | mxbai-embed-large (Ollama) |
| Vector DB     | ChromaDB                   |
| RAG Framework | LangChain                  |
| UI            | Streamlit                  |
| Dataset       | Yelp Academic Open Dataset |

# Output

https://drive.google.com/file/d/1ut47COhxKixWsZ5OpvvXKjOsvhZ8-0qh/view?usp=sharing
