import streamlit as st
import pickle
import requests
import pandas as pd



def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=87003816640f145af61e632fbecef2c6')
    data=response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']    #poster path is the heading for poster if you check it's json file



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recom_movies = []
    recom_movies_posters=[]


    for x in movies_list:
        recom_movies.append(movies.iloc[x[0]].title)
        movie_id = movies.iloc[x[0]].id
        # FETCH POSTER FROM API using movie_id
        recom_movies_posters.append(fetch_poster(movie_id))

    return recom_movies, recom_movies_posters




# with open("movies.pkl", "rb") as file1:
#     movies = pickle.load(file1)
movies = pd.read_pickle("movies.pkl")
# with open("similarity.pkl", "rb") as file2:
#     similarity = pickle.load(file2)
similarity = pd.read_pickle("similarity.pkl")


#TITLE
st.title('Which movie best suits you ?? 🤔')
st.write("\n\n")

#SELECT BOX
selected_movie = st.selectbox(
    'Which movie do you like?',
    movies['title'].values)

#BUTTON
if st.button('Search'):
    st.write("\n")
    st.write('🫡 Top 5 Movies which suits you:')
    st.write("\n")
    names, posters = recommend(selected_movie)

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








# streamlit run Web_App.py