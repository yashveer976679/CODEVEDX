import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
movies = pd.read_csv("movies.csv")

# Keep only required columns
movies = movies[["title", "genres", "keywords", "overview", "vote_average", "release_date"]]

# Replace missing values
movies.fillna("", inplace=True)

# Combine important text features
movies["tags"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["overview"]
)

# Convert text into numbers
tfidf = TfidfVectorizer(stop_words="english")

movie_vectors = tfidf.fit_transform(movies["tags"])

# Calculate similarity
similarity = cosine_similarity(movie_vectors)

print("Recommendation Model Ready!")


def recommend(movie_name):

    movie_name = movie_name.lower()

    matches = movies[movies["title"].str.lower() == movie_name]

    if matches.empty:
        print("Movie not found!")
        return

    movie_index = matches.index[0]

    distances = list(enumerate(similarity[movie_index]))

    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0

    for movie in distances[1:]:

        index = movie[0]

        score = movie[1]

        title = movies.iloc[index]["title"]

        rating = movies.iloc[index]["vote_average"]

        year = str(movies.iloc[index]["release_date"])[:4]

        print(f"{count+1}. {title} ({year}) ⭐ {rating} | Similarity: {round(score*100,2)}%")

        count += 1

        if count == 5:
            break


while True:

    print("\n==============================")
    movie = input("Enter Movie Name (or type exit): ")

    if movie.lower() == "exit":
        break

    recommend(movie)