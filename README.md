# 🎥 Watch-It Movie-Revenue Prediction

This repository provides a **FastAPI** backend and a **Streamlit** frontend for predicting whether a movie will generate **High** or **Low** revenue based on its features. The application leverages a **Gradient Boosting Model** trained on historical movie data.

---

## 📂 Project Structure
   ```bash
   /movie-revenue-prediction
   |-- app.py                         # FastAPI backend
   |-- watch-it_model.pkl             # Trained machine learning model
   |-- streamlit_app.py               # Streamlit frontend
   |-- requirements.txt               # Python dependencies
   |-- README.md                      # Project documentation

   ```

---

## 🚀 Features

1. **Backend (FastAPI)**:
   - Exposes a `/predict/` endpoint for predicting movie revenue categories.
   - Accepts both required and optional features as input.
   - Outputs a prediction of either **High** or **Low** revenue.

2. **Frontend (Streamlit)**:
   - User-friendly interface for entering movie data.
   - Sends input to the FastAPI backend and displays predictions.

3. **Machine Learning Model**:
   - Trained using a Gradient Boosting algorithm.
   - Features include runtime, votes, IMDB rating, and others.

---

## 📦 Dependencies

- **Backend**:
  - `fastapi`
  - `uvicorn`
  - `pandas`
  - `scikit-learn`

- **Frontend**:
  - `streamlit`
  - `requests`

Install all dependencies using:
```bash
pip install -r requirements.txt
```

# ⚙️ Usage
1. Run Backend Locally
Start the FastAPI server using uvicorn:

```bash
uvicorn app:app --reload
```
Access the Swagger documentation at: https://movie-revenue-prediction-ygbp.onrender.com/docs/

2. Run Frontend Locally
Start the Streamlit app:

```bash
streamlit run streamlit_app.py
```
Access the app at: https://movie-revenue-prediction-equh8ryt3apptgtpgkb2jvm.streamlit.app/

3. Test Prediction
Enter movie features in the Streamlit app or use tools like Postman to send a request to the FastAPI backend.
Example curl request:
```bash
Copy code
curl -X POST -H "Content-Type: application/json" \
-d '{"country": "USA", "genres": "Action", "runtime": 120, "users_votes": 1500, "ratings_imdb": 8.1, "ratings_tomatoes": 85, "ratings_metacritic": 75, "number_of_countries": 1}' \
https://movie-revenue-prediction-ygbp.onrender.com//predict/
```

## 🌐 Deployment

### Backend Deployment (Render)
1. Push your repository to GitHub.
2. Create a new **Web Service** on [Render](https://render.com/).
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host=0.0.0.0 --port=$PORT`
4. Access your backend at the provided Render URL.

### Frontend Deployment (Streamlit Cloud)
1. Push `streamlit_app.py` to the same GitHub repository.
2. Deploy the Streamlit app on [Streamlit Cloud](https://streamlit.io/cloud).
3. Update the `api_url` in `streamlit_app.py` to point to the deployed FastAPI URL.

### 🔑 API Details

#### **Endpoint: `/predict/` (POST)**

- **Description**: Predicts whether a movie generates high or low revenue.
- **Request Format**: JSON object with movie features.
- **Response Format**: JSON object with prediction result.

---

#### **🧪 Example Inputs**
Required Features
```json
{
    "country": "USA",
    "genres": "Action",
    "runtime": 120.0,
    "users_votes": 1500.0,
    "ratings_imdb": 8.1,
    "ratings_tomatoes": 85.0,
    "ratings_metacritic": 75.0,
    "number_of_countries": 1
}
```
Optional Features
```json
{
    "language": "English",
    "writer_count": 2.0,
    "title_adaption": "Original",
    "censor_rating": "PG",
    "comments": 50.0,
    "likes": 300.0,
    "overall_views": 5000.0,
    "dislikes": 10.0,
    "special_award": 1,
    "awards_win": 2,
    "awards_nomination": 5,
    "month_to_dvd_release": 3,
    "release_month": "June",
    "release_quarter": "Q2",
    "engagement_ratio": 0.75,
    "feedback_ratio": 0.85,
    "award_nomination_win_ratio": 0.4,
    "number_of_genres": 2,
    "number_of_languages": 1.0
}
```
Output
```json
{
    "revenue_category": "High"
}
```

# 🛠️ Troubleshooting
### Common Issues
1. Streamlit Error: Unable to fetch prediction:
- Ensure the backend URL (api_url) is correct.
- Confirm the FastAPI server is running.
- 
2. FastAPI Error: Specifying the columns using strings is only supported for dataframes:
- Check if input data is converted into a DataFrame with correct column names.

# 👥 Contributors
- [Omotayo Ikudayisi](https://github.com/Glitzzybetty/).
- Let's collaborate for future projects, buzzzzz me 
- Feel free to fork, enhance, or report issues.


# 📄 License
This project is licensed under the MIT License. See LICENSE for details.
