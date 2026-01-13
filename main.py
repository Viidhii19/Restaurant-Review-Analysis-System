from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import positive_retriever, negative_retriever

model = OllamaLLM(model="llama3.2")


def get_recommendation(pos_count, neg_count):
    if pos_count == 0 and neg_count == 0:
        return "Not Recommend (Insufficient Data)"
    if neg_count > pos_count:
        return "Not Recommend"
    return "Recommend"


template = """
You are a restaurant review analyst.

You are given POSITIVE and NEGATIVE customer reviews.

Your task:
1. Start with the Recommendation flag
2. Give an overall verdict (Good / Average / Bad / Insufficient Data)
3. Evaluate:
   - Food quality
   - Ambience
   - Service & management
4. Mention common praises
5. Mention common complaints
6. Be honest. No exaggeration.

POSITIVE REVIEWS:
{positive_reviews}

NEGATIVE REVIEWS:
{negative_reviews}

Recommendation: {recommendation}

User question:
{question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    print("\n-------------------------------")
    question = input("Ask your question (q to quit): ")

    if question.lower() == "q":
        break

    pos_reviews = positive_retriever.invoke(question)
    neg_reviews = negative_retriever.invoke(question)

    recommendation = get_recommendation(len(pos_reviews), len(neg_reviews))

    result = chain.invoke({
        "positive_reviews": pos_reviews,
        "negative_reviews": neg_reviews,
        "recommendation": recommendation,
        "question": question
    })

    print("\nANSWER:\n")
    print(result)
