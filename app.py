# app.py
import streamlit as st
from vector import get_filtered_reviews, get_restaurant_names, get_all_cuisines, get_restaurant_info
from router import route_question
import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background: url(data:image/jpg;base64,{encoded});
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    .main .block-container {{
        background-color: rgba(0, 0, 0, 0.75);
        padding: 3rem;
        border-radius: 15px;
        color: white;
    }}
    h1, h2, h3, h4, h5, h6, .stMarkdown, p, label {{
        color: white !important;
    }}
    .stSelectbox label, .stTextInput label {{
        color: white !important;
        font-weight: bold;
    }}
    div[data-baseweb="select"] > div {{
        background-color: white; 
        color: black;
    }}
    div[data-baseweb="input"] > div {{
        background-color: white; 
        color: black;
    }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)
set_background("background.jpg")

st.set_page_config(page_title="Restaurant Review Analysis System", page_icon="🍽")


st.title("Restaurant Review Analysis System")

# 1. Cuisine Filter
cuisines = ["All"] + get_all_cuisines()
selected_cuisine = st.selectbox("Filter by Cuisine", cuisines)

# 2. Restaurant Selection (Filtered)
restaurants = get_restaurant_names(cuisine=selected_cuisine)

if not restaurants:
    st.warning("No restaurants available right now.")
    restaurant = None
else:
    restaurant = st.selectbox("Select Restaurant", restaurants)
    if restaurant:
        info = get_restaurant_info(restaurant)
        if info and "business_rating" in info:
            try:
                rating = float(info["business_rating"])
                full_stars = int(rating)
                half_star = 1 if rating - full_stars >= 0.5 else 0
                stars_str = "⭐" * full_stars + ("✨" if half_star else "")
                st.subheader(f"{restaurant}  {stars_str} ({rating}/5)")
                st.write(f"**Cuisine:** {info.get('cuisine', 'Unknown')} | **Location:** {info.get('city', '')}, {info.get('state', '')}")
            except Exception:
                st.subheader(restaurant)
        else:
            st.subheader(restaurant)

question = st.text_input("Ask a question", "How is the overall experience?")

if st.button("Analyze"):
    docs = get_filtered_reviews(question, restaurant, sentiment=None, k=20)

    skill_name, skill_fn = route_question(question)

    if len(docs) == 0:
        st.error("No reviews found for this restaurant.")
    else:
        st.write(skill_fn(docs))
