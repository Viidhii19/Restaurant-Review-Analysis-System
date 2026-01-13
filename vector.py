from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

DB_DIR = "yelp_chroma_db"

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

vector_store = Chroma(
    collection_name="yelp_reviews",
    persist_directory=DB_DIR,
    embedding_function=embeddings,
)

from skills.cuisine_constants import VALID_CUISINES

def get_filtered_reviews(query, restaurant=None, sentiment=None, k=20):
    filters = {}

    if restaurant:
        filters["restaurant"] = restaurant

    if sentiment:
        filters["sentiment"] = sentiment

    return vector_store.similarity_search(
        query=query,
        k=k,
        filter=filters or None
    )

def get_restaurant_names(cuisine=None):
    """
    Returns a sorted list of unique restaurant names.
    If `cuisine` is provided, filters by that cuisine type from metadata.
    """
    # 1. Get raw metadatas
    metas = vector_store._collection.get(include=["metadatas"], limit=1000000)["metadatas"]
    
    unique_names = set()
    
    for m in metas:
        if "restaurant" not in m:
            continue
            
        # Filter if a specific cuisine is requested
        if cuisine and cuisine != "All":
            # Split the restaurant's cuisine string into a list of cleaned categories
            db_cuisines = [c.strip() for c in m.get("cuisine", "").split(",")]
            if cuisine not in db_cuisines:
                continue
            
        unique_names.add(m["restaurant"])
        
    return sorted(unique_names)


def get_all_cuisines():
    """
    Returns a sorted list of all unique cuisines found in metadata.
    """

    metas = vector_store._collection.get(include=["metadatas"], limit=1000000)["metadatas"]
    cuisines = set()
    
    for m in metas:
        if "cuisine" in m and m["cuisine"]:
            # Split by comma and strip whitespace to get individual cuisines
            parts = m["cuisine"].split(",")
            for part in parts:
                cleaned = part.strip()
                if cleaned in VALID_CUISINES:
                    cuisines.add(cleaned)
            
    return sorted(list(cuisines))

def get_restaurant_info(restaurant_name):
    """
    Retrieves metadata for a specific restaurant.
    """
    results = vector_store.similarity_search(
        query="",
        k=1,
        filter={"restaurant": restaurant_name}
    )
    
    if results:
        return results[0].metadata
    return {}

