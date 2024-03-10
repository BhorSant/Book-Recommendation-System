import pickle
import streamlit as st
import numpy as np
import seaborn as sns
st.header("Book Recommendation System using Machine Learning")

st.sidebar.header("User Profile")

user_name = st.sidebar.text_input("Enter your name")

st.sidebar.header("User Profile")

st.sidebar.subheader(user_name)
# Used model

model = pickle.load(open("artifacts\model.pkl", "rb"))
books_name = pickle.load(open("artifacts\books.pkl", "rb"))
book_pivot = pickle.load(open("artifacts\book_pivot.pkl", "rb"))
final_rating = pickle.load(open("artifacts\final_rating.pkl","rb"))


