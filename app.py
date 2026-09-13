import streamlit as st
import pickle
import requests

st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load data
movies = pickle.load(open("movies_list.pkl", "rb"))
movies_list = movies["title"].values
similarity = pickle.load(open("similarity.pkl", "rb"))


# Header
st.markdown(
    '<div class="main-title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Discover movies you might enjoy</div>',
    unsafe_allow_html=True
)


# Movie selection
select_value = st.selectbox(
    "Select movie from dropdown",
    movies_list
)


def fetch_poster(movie_id):

    api_key = st.secrets["TMDB_API_KEY"]

    url = (
        "https://api.themoviedb.org/3/movie/{}"
        "?api_key={}"
        "&language=en-US"
    ).format(movie_id, api_key)

    data = requests.get(url)
    data = data.json()

    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]

    distance = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda vector: vector[1]
    )

    recommend_movie = []
    recommend_poster = []

    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].id

        recommend_movie.append(
            movies.iloc[i[0]].title
        )

        recommend_poster.append(
            fetch_poster(movie_id)
        )

    return recommend_movie, recommend_poster


# Recommend button
if st.button("Show Recommend"):

    movie_name, movie_poster = recommend(select_value)

    st.markdown(
        '<div class="recommend-title">Recommended Movies</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(5)

    for i, col in enumerate(cols):

        with col:

            st.markdown(
                f"""
                <div class="movie-card">
                    <div class="movie-title">
                        {movie_name[i]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.image(
                movie_poster[i],
                use_container_width=True
            )