import pickle
from flask import Flask, request, jsonify

# Load the model
with open("watch-it_model.pkl", "rb") as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # Get JSON input
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Extract features (assumes the input is a dictionary of features)
    try:
        features = data["features"]
    except KeyError:
        return jsonify({"error": "Missing 'features' key"}), 400

    # Make prediction
    prediction = model.predict([features])[0]

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
