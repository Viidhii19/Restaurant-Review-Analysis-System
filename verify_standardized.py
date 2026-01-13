from vector import get_all_cuisines, get_restaurant_names
from skills.cuisine_constants import VALID_CUISINES

print("--- Testing get_all_cuisines with Allow-List ---")
cuisines = get_all_cuisines()
print(f"Total allowed cuisines found: {len(cuisines)}")
print("First 20 cuisines:")
print(cuisines[:20])

# Verify no junk
junk_terms = ["Restaurants", "Food", "Nightlife", "Bars"]
for junk in junk_terms:
    if junk in cuisines:
        print(f"❌ FAILED: Junk term '{junk}' found in list!")
    else:
        print(f"✅ PASSED: Junk term '{junk}' correctly filtered out.")

# Verify valid items
if "Chinese" in cuisines:
    print("✅ PASSED: 'Chinese' found in list.")
else:
    print("❌ FAILED: 'Chinese' missing from list.")

# Check filtering
test_cuisine = "Italian" if "Italian" in cuisines else (cuisines[0] if cuisines else None)
if test_cuisine:
    print(f"\n--- Testing get_restaurant_names for '{test_cuisine}' ---")
    restaurants = get_restaurant_names(cuisine=test_cuisine)
    print(f"Found {len(restaurants)} restaurants.")
