from flask import Flask, render_template, request
import pandas as pd
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# ----------------------------
# Load Dataset
# ----------------------------
movies = pd.read_csv("movies.csv")

movies = movies[
    [
        "title",
        "genres",
        "keywords",
        "overview",
        "vote_average",
        "release_date"
    ]
]

movies.fillna("", inplace=True)


# ----------------------------
# Convert JSON text into names
# ----------------------------
def extract_names(text):
    try:
        items = ast.literal_eval(text)
        return " ".join(item["name"] for item in items)
    except:
        return ""


movies["genres"] = movies["genres"].apply(extract_names)
movies["keywords"] = movies["keywords"].apply(extract_names)

movies["tags"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["overview"]
)

# ----------------------------
# TF-IDF
# ----------------------------
vectorizer = TfidfVectorizer(stop_words="english")

movie_vectors = vectorizer.fit_transform(movies["tags"])

similarity = cosine_similarity(movie_vectors)

POPULAR_MOVIES = [
    "Avatar",
    "Iron Man",
    "Interstellar",
    "The Avengers",
    "The Dark Knight",
    "Titanic",
    "Inception",
    "Spider-Man"
]


# ----------------------------
# Recommendation Function
# ----------------------------
def recommend(movie_name):

    movie_name = movie_name.lower().strip()

    matches = movies[
        movies["title"]
        .str.lower()
        .str.contains(movie_name, na=False)
    ]

    if matches.empty:
        return None

    movie_index = matches.index[0]

    distances = list(enumerate(similarity[movie_index]))

    distances = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for movie in distances[1:7]:

        idx = movie[0]

        recommendations.append({

            "title":
                movies.iloc[idx]["title"],

            "rating":
                round(float(movies.iloc[idx]["vote_average"]),1),

            "year":
                str(movies.iloc[idx]["release_date"])[:4],

            "overview":
                movies.iloc[idx]["overview"][:220] + "...",

            "genres":
                movies.iloc[idx]["genres"],

            "similarity":
                round(movie[1]*100,2)

        })

    return recommendations


# ----------------------------
# Home Page
# ----------------------------
@app.route("/", methods=["GET","POST"])

def home():

    recommendations=[]

    searched_movie=""

    not_found=False

    if request.method=="POST":

        searched_movie=request.form["movie"]

        recommendations=recommend(searched_movie)

        if recommendations is None:

            recommendations=[]

            not_found=True

    return render_template(

        "index.html",

        recommendations=recommendations,

        searched_movie=searched_movie,

        not_found=not_found,

        total_movies=len(movies),

        popular_movies=POPULAR_MOVIES

    )


if __name__=="__main__":

    app.run(debug=True)