import streamlit as st
import pickle

# Load movie data and similarity matrix
movies = pickle.load(open("movies.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Set page title and favicon
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬"
)

# Set a wider page layout for better readability
st.markdown(
    """
    <style>
        .main {
            max-width: 1200px;
            padding-top: 4rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header with improved styling
st.title("🎬 Movie Recommender System")

# Selectbox for movie selection
select_value = st.selectbox("🍿 Select a movie from the dropdown", movies_list)

# Function to recommend movies based on user selection
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error(f"Movie '{movie}' not found. Please select a different movie.")
        return []

    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movies = [movies.iloc[i[0]].title for i in distance[1:11]]
    return recommended_movies

# Button to trigger movie recommendations
if st.button("🚀 Show Movie Suggestions"):
    recommended_movies = recommend(select_value)
    if recommended_movies:
        st.markdown("## 🎉 Recommended Movies")

        # Create a grid layout for better organization
        col1, col2 = st.columns(2)

        for i, movie in enumerate(recommended_movies, start=1):
            col1.write(f"{i}. {movie}")

