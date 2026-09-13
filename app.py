import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", "rb"))
movies_list = movies["title"].values

st.header("Movie Recommendation System")
st.selectbox("Select movie from dropdown", movies_list)
if st.button("Show Recommend"):
    pass