import streamlit as st
import requests

# Title of the app
st.title("Movie Revenue Prediction App")
st.markdown(
    """
    This app predicts whether a movie will generate **High** or **Low** revenue based on key features.
    Provide the required information below and click **Predict**.
    """
)

# Input fields
st.header("Enter Movie Features")
country = st.text_input("Country", "USA")
genres = st.text_input("Genres", "Action")
runtime = st.number_input("Runtime (minutes)", min_value=1, step=1, value=120)
users_votes = st.number_input("Number of Users Votes", min_value=0, step=1, value=100)
ratings_imdb = st.number_input("IMDB Rating", min_value=0.0, max_value=10.0, step=0.1, value=7.5)
ratings_tomatoes = st.number_input("Rotten Tomatoes Rating", min_value=0.0, max_value=100.0, step=1.0, value=85.0)
ratings_metacritic = st.number_input("Metacritic Rating", min_value=0.0, max_value=100.0, step=1.0, value=80.0)
number_of_countries = st.number_input("Number of Countries", min_value=1, step=1, value=1)

# Backend API URL
api_url = "https://movie-revenue-prediction-ygbp.onrender.com/predict/"

# Prediction button
if st.button("Predict Revenue Category"):
    # Prepare the data payload
    data = {
        "country": country,
        "genres": genres,
        "runtime": runtime,
        "users_votes": users_votes,
        "ratings_imdb": ratings_imdb,
        "ratings_tomatoes": ratings_tomatoes,
        "ratings_metacritic": ratings_metacritic,
        "number_of_countries": number_of_countries,
    }

    # Make the API request
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['revenue_category']}")
    else:
        st.error("Error: Unable to fetch prediction.")
