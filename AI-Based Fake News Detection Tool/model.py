import joblib

# Load trained model
model = joblib.load("saved_model.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("vectorizer.pkl")


def detect_news(news_text):
    # Convert text into vector
    text_vector = vectorizer.transform([news_text])

    # Prediction
    prediction = model.predict(text_vector)[0]

    # Confidence
    confidence = model.predict_proba(text_vector).max() * 100

    if prediction == 1:
        label = "REAL NEWS"
    else:
        label = "FAKE NEWS"

    return label, round(confidence, 2)