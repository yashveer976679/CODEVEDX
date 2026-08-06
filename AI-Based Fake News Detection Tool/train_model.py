import pandas as pd
import re
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# -----------------------------
# Text Cleaning Function
# -----------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

# -----------------------------
# Load Dataset
# -----------------------------
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Labels
fake["label"] = 0
true["label"] = 1

# Keep required columns
fake = fake[["title", "text", "label"]]
true = true[["title", "text", "label"]]

# Merge title and text
fake["content"] = fake["title"] + " " + fake["text"]
true["content"] = true["title"] + " " + true["text"]

# Clean text
fake["content"] = fake["content"].apply(clean_text)
true["content"] = true["content"].apply(clean_text)

# Keep only required columns
fake = fake[["content", "label"]]
true = true[["content", "label"]]

# Merge datasets
data = pd.concat([fake, true], ignore_index=True)

# Shuffle data
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Features and Labels
X = data["content"]
y = data["label"]

# -----------------------------
# TF-IDF
# -----------------------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=10000,
    ngram_range=(1,2)
)

X = vectorizer.fit_transform(X)

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# -----------------------------
# Accuracy
# -----------------------------
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy*100:.2f}%")

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "saved_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel trained successfully!")
print("saved_model.pkl created")
print("vectorizer.pkl created")