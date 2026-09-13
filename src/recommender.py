import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

def recommand(movie):
    index = movies[movies["title"] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda vector : vector[1])
    for i in distance[0:5]:
        print(movies.iloc[i[0]].title)


movies = pd.read_csv("../dataset/movies.csv")

movies = movies[["id", "title", "genre", "overview"]]
movies["tags"] = movies["overview"] + " " + movies["genre"]
movies = movies.drop(columns = ["overview", "genre"])

vectorizer = TfidfVectorizer()
vector = vectorizer.fit_transform(movies["tags"].values.astype("U")).toarray()

similarity = cosine_similarity(vector)


pickle.dump(movies, open("../movies_list.pkl", "wb"))
pickle.dump(similarity, open("../similarity.pkl", "wb"))