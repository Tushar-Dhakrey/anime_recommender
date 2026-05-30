# Anime Recommendation System

## Project Overview

This project implements an Anime Recommendation System using multiple recommendation techniques. The system recommends anime based on genre similarity, user rating behavior, and a hybrid approach that combines both methods.

The project also includes a Streamlit web application that allows users to interactively discover anime recommendations along with anime posters fetched using the Jikan API.

---

## Features

* Content-Based Recommendation System
* Collaborative Filtering using K-Nearest Neighbors (KNN)
* Hybrid Recommendation System
* Interactive Streamlit Web Application
* Anime Poster Integration using Jikan API
* Genre-Based Similarity Search
* User Rating-Based Recommendations

---

## Dataset

Dataset files:

* anime.csv
* rating.csv

The dataset contains:

* Anime titles
* Genres
* Community ratings
* User ratings
* Anime metadata

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Requests
* Jupyter Notebook

---

## Content-Based Filtering

The content-based recommender uses anime genres to identify similar anime.

### Techniques Used

* Genre Preprocessing
* CountVectorizer
* Cosine Similarity

The system recommends anime with similar content and genre characteristics.

---

## Collaborative Filtering

The collaborative recommender learns from user rating patterns.

### Techniques Used

* User-Anime Pivot Table
* Sparse Matrix Representation
* K-Nearest Neighbors (KNN)

The system recommends anime that are liked by users with similar preferences.

---

## Hybrid Recommendation System

The hybrid recommender combines:

* Content-Based Recommendations
* Collaborative Filtering Recommendations

Duplicate recommendations are removed to generate a stronger final recommendation list.

---

## Streamlit Web Application

The project includes a Streamlit-based web application.

### Features

* Anime Selection Dropdown
* Content-Based Recommendations
* Collaborative Recommendations
* Hybrid Recommendations
* Anime Poster Display
* Interactive User Interface

### Run the Application

```bash
streamlit run app.py
```

---

## API Integration

This project uses the Jikan API to fetch anime posters dynamically from MyAnimeList.

The API is used to:

* Search anime information
* Retrieve anime poster URLs
* Display posters in the Streamlit application

---

## Project Structure

```text
anime_recommender/
│
├── app.py
├── anime_recommand.ipynb
├── anime.csv
├── rating.csv
├── README.md
├── requirements.txt
└── .gitignore
```

## Author

Tushar Dhakrey
