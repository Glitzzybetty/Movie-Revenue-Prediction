import streamlit as st
import requests

# Set API URL
api_url = "https://movie-revenue-prediction-ygbp.onrender.com/predict/"

# Title and description
st.title("Movie Revenue Prediction App")
st.markdown(
    """
    This app predicts whether a movie will generate **High** or **Low** revenue based on its features.
    Provide the required information below and optionally add other details for better predictions.
    """
)

# Input fields for required features
st.header("Required Movie Features")
country = st.text_input("Country", "USA")
genres = st.text_input("Genres", "Action")
runtime = st.number_input("Runtime (minutes)", min_value=1.0, step=1.0, value=120.0)
users_votes = st.number_input("Number of Users Votes", min_value=0.0, step=1.0, value=100.0)
ratings_imdb = st.number_input("IMDB Rating", min_value=0.0, max_value=10.0, step=0.1, value=7.5)
ratings_tomatoes = st.number_input("Rotten Tomatoes Rating", min_value=0.0, max_value=100.0, step=1.0, value=85.0)
ratings_metacritic = st.number_input("Metacritic Rating", min_value=0.0, max_value=100.0, step=1.0, value=80.0)
number_of_countries = st.number_input("Number of Countries", min_value=1, step=1, value=1)

# Input fields for optional features
st.header("Optional Movie Features")
language = st.text_input("Language", "")
writer_count = st.number_input("Number of Writers", min_value=0.0, step=1.0, value=0.0)
title_adaption = st.text_input("Title Adaption (Original/Adapted)", "")
censor_rating = st.text_input("Censor Rating (e.g., PG, R, etc.)", "")
comments = st.number_input("Number of Comments", min_value=0.0, step=1.0, value=0.0)
likes = st.number_input("Number of Likes", min_value=0.0, step=1.0, value=0.0)
overall_views = st.number_input("Overall Views", min_value=0.0, step=1.0, value=0.0)
dislikes = st.number_input("Number of Dislikes", min_value=0.0, step=1.0, value=0.0)
special_award = st.number_input("Special Award Count", min_value=0, step=1, value=0)
awards_win = st.number_input("Awards Won", min_value=0, step=1, value=0)
awards_nomination = st.number_input("Awards Nominated", min_value=0, step=1, value=0)
month_to_dvd_release = st.number_input("Months to DVD Release", min_value=0, step=1, value=0)
release_month = st.text_input("Release Month", "")
release_quarter = st.text_input("Release Quarter (Q1, Q2, etc.)", "")
engagement_ratio = st.number_input("Engagement Ratio", min_value=0.0, max_value=1.0, step=0.01, value=0.0)
feedback_ratio = st.number_input("Feedback Ratio", min_value=0.0, max_value=1.0, step=0.01, value=0.0)
award_nomination_win_ratio = st.number_input("Award Nomination Win Ratio", min_value=0.0, max_value=1.0, step=0.01, value=0.0)
number_of_genres = st.number_input("Number of Genres", min_value=1, step=1, value=1)
number_of_languages = st.number_input("Number of Languages", min_value=0.0, step=1.0, value=0.0)

# Prediction button
if st.button("Predict Revenue Category"):
    # Prepare the data payload
    data = {
        "country": country,
        "genres": genres,
        "language": language,
        "writer_count": writer_count,
        "title_adaption": title_adaption,
        "censor_rating": censor_rating,
        "runtime": runtime,
        "users_votes": users_votes,
        "comments": comments,
        "likes": likes,
        "overall_views": overall_views,
        "dislikes": dislikes,
        "ratings_imdb": ratings_imdb,
        "ratings_tomatoes": ratings_tomatoes,
        "ratings_metacritic": ratings_metacritic,
        "special_award": special_award,
        "awards_win": awards_win,
        "awards_nomination": awards_nomination,
        "month_to_dvd_release": month_to_dvd_release,
        "release_month": release_month,
        "release_quarter": release_quarter,
        "engagement_ratio": engagement_ratio,
        "feedback_ratio": feedback_ratio,
        "award_nomination_win_ratio": award_nomination_win_ratio,
        "number_of_genres": number_of_genres,
        "number_of_languages": number_of_languages,
        "number_of_countries": number_of_countries,
    }

    # Make the API request
    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['revenue_category']}")
        else:
            st.error(f"Error: {response.json()['detail']}")
    except Exception as e:
        st.error(f"Connection Error: {e}")
