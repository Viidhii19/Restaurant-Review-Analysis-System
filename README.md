# 🍽️ Restaurant Review Intelligence System (RAG-Based)

An end-to-end **Retrieval-Augmented Generation (RAG)** system that transforms thousands of raw restaurant reviews into **trustworthy, evidence-backed insights** using LLMs.

Unlike typical AI apps that hallucinate, this system ensures every answer is **grounded in real customer reviews**.

---

## 🚀 Why This Project Matters

Choosing a restaurant today means scanning hundreds of reviews across platforms.

This system eliminates that friction by allowing users to ask:

* “Is this place good for business meetings?”
* “Are customers complaining about service delays?”
* “Is the pricing justified by quality?”

…and receive **fact-based answers backed by real user reviews**.

---

## ⚡ Key Features

* 🔍 **Semantic Search over Reviews** (not keyword-based)
* 🧠 **RAG Pipeline** for grounded responses
* 🎯 **Intent-Aware Query Routing** (food, pricing, service, ambience)
* 📊 **Evidence-Based Answers** with source transparency
* 💬 **Natural Language Q&A Interface**
* ⚡ Real-time interaction via Streamlit

---

## 🧠 System Architecture

Pipeline Overview:

1. **Data Ingestion**

   * Yelp Academic Dataset (business + reviews)

2. **Preprocessing**

   * Restaurant filtering
   * Text cleaning & normalization
   * Metadata linking

3. **Embedding Layer**

   * Model: `mxbai-embed-large`
   * Converts reviews → dense vectors

4. **Vector Storage**

   * ChromaDB for efficient similarity search

5. **Retriever**

   * Semantic search retrieves top-k relevant reviews

6. **Intent Router**

   * Classifies query into categories:

     * Food, Service, Price, Ambience, Trends

7. **LLM Reasoning**

   * Model: LLaMA 3.2 (via Ollama)
   * Generates answers strictly from retrieved context

8. **User Interface**

   * Streamlit-based interactive dashboard

---

## 📊 Example Output

🎥 Demo:
https://drive.google.com/file/d/1ut47COhxKixWsZ5OpvvXKjOsvhZ8-0qh/view?usp=sharing

---

## 🧪 What Makes This Different

Most beginner RAG projects:

* Dump documents into a vector DB
* Ask questions → generate answers

This project goes further:

* ✅ **Intent-aware routing before generation**
* ✅ **Structured restaurant filtering (not generic corpus)**
* ✅ **End-to-end pipeline (data → UI)**
* ✅ **Focus on real-world decision-making use case**

---

## ⚙️ Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Language   | Python                |
| LLM        | LLaMA 3.2 (Ollama)    |
| Embeddings | mxbai-embed-large     |
| Vector DB  | ChromaDB              |
| Framework  | LangChain             |
| UI         | Streamlit             |
| Dataset    | Yelp Academic Dataset |

---

## 📌 Limitations

* Performance depends on embedding quality
* No fine-tuning applied (pure RAG pipeline)
* Limited to dataset coverage (no live reviews)

---

## 🚧 Future Improvements

* Hybrid search (BM25 + embeddings)
* Fine-tuned LLM for better reasoning
* Real-time data ingestion (Google/Yelp APIs)
* Personalized recommendations per user

---

## 🧠 Key Takeaways

This project demonstrates:

* Practical implementation of RAG systems
* Understanding of LLM limitations (hallucination)
* Ability to design **data → retrieval → reasoning pipelines**
* Building **AI systems with real-world usability**
