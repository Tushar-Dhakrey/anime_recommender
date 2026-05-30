import streamlit as st
import pickle
import numpy as np
import requests

# Load Pickle Files

anime_df = pickle.load(open('anime_df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

pt = pickle.load(open('pivot_table.pkl', 'rb'))
model = pickle.load(open('knn_model.pkl', 'rb'))

# Fetch Anime Poster

def fetch_poster(anime_name):

    try:
        url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"

        response = requests.get(url)

        data = response.json()

        poster = data['data'][0]['images']['jpg']['image_url']

        return poster

    except:
        return None


# Content Based

def recommend_content(anime):

    anime_index = anime_df[
        anime_df['name'] == anime
    ].index[0]

    distances = similarity[anime_index]

    anime_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []
    posters = []

    for i in anime_list:

        anime_name = anime_df.iloc[i[0]]['name']

        recommendations.append(anime_name)

        posters.append(
            fetch_poster(anime_name)
        )

    return recommendations, posters


# Collaborative Filtering


def recommend_collab(anime_name):

    anime_index = np.where(
        pt.index == anime_name
    )[0][0]

    distances, suggestions = model.kneighbors(
        pt.iloc[anime_index, :]
        .values
        .reshape(1, -1),
        n_neighbors=6
    )

    recommendations = []
    posters = []

    for i in suggestions[0][1:]:

        anime_name = pt.index[i]

        recommendations.append(anime_name)

        posters.append(
            fetch_poster(anime_name)
        )

    return recommendations, posters


# Hybrid

def recommend_hybrid(anime):

    content_names, _ = recommend_content(anime)

    collab_names, _ = recommend_collab(anime)

    hybrid = content_names + collab_names

    hybrid = list(
        dict.fromkeys(hybrid)
    )

    hybrid = hybrid[:10]

    posters = []

    for name in hybrid:

        posters.append(
            fetch_poster(name)
        )

    return hybrid, posters


# Streamlit UI

st.title("Anime Recommendation System")

anime_list = sorted(
    anime_df['name'].unique()
)

selected_anime = st.selectbox(
    "Select Anime",
    anime_list
)

recommender_type = st.radio(
    "Choose Recommender",
    [
        "Content-Based",
        "Collaborative",
        "Hybrid"
    ]
)

if st.button("Recommend"):

    if recommender_type == "Content-Based":

        names, posters = recommend_content(
            selected_anime
        )

    elif recommender_type == "Collaborative":

        names, posters = recommend_collab(
            selected_anime
        )

    else:

        names, posters = recommend_hybrid(
            selected_anime
        )

    st.subheader("Recommended Anime")

    cols = st.columns(5)

    for idx in range(
        min(5, len(names))
    ):

        with cols[idx]:

            st.write(names[idx])

            if posters[idx]:

                st.image(
                    posters[idx],
                    use_container_width=True
                )