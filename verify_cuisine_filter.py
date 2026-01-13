from vector import get_all_cuisines, get_restaurant_names, get_restaurant_info

print("--- Testing get_all_cuisines ---")
cuisines = get_all_cuisines()
print(f"Total cuisines found: {len(cuisines)}")
print("First 20 cuisines:")
print(cuisines[:20])

if "Chinese" in cuisines:
    test_cuisine = "Chinese"
else:
    test_cuisine = cuisines[0] if cuisines else None

if test_cuisine:
    print(f"\n--- Testing get_restaurant_names for '{test_cuisine}' ---")
    restaurants = get_restaurant_names(cuisine=test_cuisine)
    print(f"Found {len(restaurants)} restaurants for {test_cuisine}")
    
    if restaurants:
        first_restaurant = restaurants[0]
        print(f"Checking first restaurant: {first_restaurant}")
        info = get_restaurant_info(first_restaurant)
        print(f"Metadata cuisine: {info.get('cuisine')}")
        
        # Verify correctness
        if test_cuisine in [c.strip() for c in info.get("cuisine", "").split(",")]:
            print("✅ Verification SUCCESS: Restaurant has the selected cuisine.")
        else:
            print("❌ Verification FAILED: Restaurant does not match.")
else:
    print("No cuisines found to test.")
