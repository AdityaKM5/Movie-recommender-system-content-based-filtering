import pickle
import streamlit as st
import requests

def fetch_movie_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def fetch_movie():
   movie_name=[]
   movie_poster=[]
   for i in popular.index:
      movie_name.append(popular['original_title'][i])
      movie_poster.append(fetch_movie_poster(popular['tmdbId'][i]))
   return movie_name,movie_poster
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movie_names = []
    recommend_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movie_posters.append(fetch_movie_poster(movie_id))
        recommend_movie_names.append(movies.iloc[i[0]].title)

    return recommend_movie_names,recommend_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
popular= pickle.load(open('popular.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown",movie_list)

if st.button('Show Recommendation'):
    recommend_movie_names,recommend_movie_posters = recommend(selected_movie)
    column1, column2, column3, column4, column5 = st.columns(5)
    with column1:
        st.text(recommend_movie_names[0])
        st.image(recommend_movie_posters[0])
    with column2:
        st.text(recommend_movie_names[1])
        st.image(recommend_movie_posters[1])

    with column3:
        st.text(recommend_movie_names[2])
        st.image(recommend_movie_posters[2])
    with column4:
        st.text(recommend_movie_names[3])
        st.image(recommend_movie_posters[3])
    with column5:
        st.text(recommend_movie_names[4])
        st.image(recommend_movie_posters[4])

st.header('Top 30 Most Popular Movies On TMDB:')
popular_movie_name,popular_movie_poster= fetch_movie()
i=0
while i < 30:
    column1, column2, column3, column4, column5 , column6 = st.columns(6)
    with column1:
        st.text(popular_movie_name[i])
        st.image(popular_movie_poster[i])
        i+=1;
    with column2:
        st.text(popular_movie_name[i])
        st.image(popular_movie_poster[i])
        i += 1;
    with column3:
        st.text(popular_movie_name[i])
        st.image(popular_movie_poster[i])
        i += 1;
    with column4:
        st.text(popular_movie_name[i])
        st.image(popular_movie_poster[i])
        i += 1;
    with column5:
        st.text(popular_movie_name[i])
        st.image(popular_movie_poster[i])
        i += 1;
    with column6:
        st.text(popular_movie_name[i])
        st.image(popular_movie_poster[i])
        i += 1;
