import json
import pandas as pd

BUSINESS_FILE = "yelp_academic_dataset_business.json"
REVIEW_FILE   = "yelp_academic_dataset_review.json"

OUTPUT_FILE   = "restaurant_reviews_clean.csv"

restaurants = {}

print("Loading restaurant businesses...")

with open(BUSINESS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)

        categories = obj.get("categories") or ""
        if "Restaurant" not in categories:
            continue

        restaurants[obj["business_id"]] = {
            "name": obj["name"],
            "city": obj["city"],
            "state": obj["state"],
            "stars": obj["stars"],
            "address": obj.get("address", ""),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "price": obj.get("attributes", {}).get("RestaurantsPriceRange2"),
            "cuisine": categories
        }

print(f"Total restaurants found: {len(restaurants)}")

data = []

print("Linking reviews to restaurants...")

with open(REVIEW_FILE, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)

        bid = obj["business_id"]

        if bid not in restaurants:
            continue

        r = restaurants[bid]

        data.append({
            "restaurant": r["name"],
            "city": r["city"],
            "state": r["state"],
            "business_rating": r["stars"],
            "address": r["address"],
            "latitude": r["latitude"],
            "longitude": r["longitude"],
            "price": r["price"],
            "cuisine": r["cuisine"],
            "review_text": obj["text"],
            "review_rating": obj["stars"]
        })

        if len(data) >= 200000:
            break

print(f"Total linked reviews stored: {len(data)}")

df = pd.DataFrame(data)
df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved cleaned dataset to: {OUTPUT_FILE}")
