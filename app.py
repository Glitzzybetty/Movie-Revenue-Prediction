import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Load the trained model
with open("model.pkl", "rb") as file:
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

@app.post("/predict/")
def predict(data: MovieData):
    try:
        # Convert input to a DataFrame
        input_data = pd.DataFrame([data.dict()])

        # Perform prediction
        prediction = model.predict(input_data)[0]
        return {"revenue_category": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
