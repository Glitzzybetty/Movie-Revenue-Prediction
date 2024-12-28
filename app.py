import pickle
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# Load the trained model
with open("watch-it_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the FastAPI app
app = FastAPI()


# Define the input schema
class MovieData(BaseModel):
    country: str
    genres: str
    language: Optional[str] = None
    writer_count: Optional[float] = None
    title_adaption: str
    censor_rating: Optional[str] = None
    runtime: float
    users_votes: float
    comments: Optional[float] = None
    likes: Optional[float] = None
    overall_views: Optional[float] = None
    dislikes: Optional[float] = None
    ratings_imdb: float
    ratings_tomatoes: float
    ratings_metacritic: float
    special_award: int
    awards_win: int
    awards_nomination: int
    month_to_dvd_release: int
    release_month: Optional[str] = None
    release_quarter: str
    engagement_ratio: Optional[float] = None
    feedback_ratio: Optional[float] = None
    award_nomination_win_ratio: Optional[float] = None
    number_of_genres: int
    number_of_languages: Optional[float] = None
    number_of_countries: int


@app.get("/")
def home():
    return {"message": "Welcome to the Movie Revenue Prediction API!"}


@app.post("/predict/")
def predict(data: MovieData):
    try:
        # Convert input to model features
        features = [
            data.country,
            data.genres,
            data.language,
            data.writer_count,
            data.title_adaption,
            data.censor_rating,
            data.runtime,
            data.users_votes,
            data.comments,
            data.likes,
            data.overall_views,
            data.dislikes,
            data.ratings_imdb,
            data.ratings_tomatoes,
            data.ratings_metacritic,
            data.special_award,
            data.awards_win,
            data.awards_nomination,
            data.month_to_dvd_release,
            data.release_month,
            data.release_quarter,
            data.engagement_ratio,
            data.feedback_ratio,
            data.award_nomination_win_ratio,
            data.number_of_genres,
            data.number_of_languages,
            data.number_of_countries,
        ]
        # Predict revenue category
        prediction = model.predict([features])[0]
        return {"revenue_category": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
