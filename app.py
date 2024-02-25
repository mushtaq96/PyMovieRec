import streamlit as st
import pickle
import pandas as pd
import requests
from tmdbv3api import TMDb
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
# access the api key
TMDb_API_KEY = os.getenv('TMDb_API_KEY')

# Initialize TMDb API
tmdb = TMDb()

# Load precomputed data
with open('movie_list.pkl', 'rb') as f:
    movies = pickle.load(f)
movies_list = movies['title'].values

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

def fetch_poster(movie_id):
    """Fetch movie poster from TMDb API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDb_API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

def recommend(movie):
    """Generate movie recommendations based on precomputed similarity data."""
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:  # top 5
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

def main():
    """Main function for Streamlit app."""
    st.title('Movie Recommender System ')
    
    selected_movie_name = st.selectbox('Please enter the movie name',
                                       movies_list)
    
    if st.button("Recommend"):
        names, posters = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])

        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])

if __name__ == '__main__':
    main()
