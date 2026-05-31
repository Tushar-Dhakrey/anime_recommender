# Anime Recommendation System

A Machine Learning-based Anime Recommendation System that recommends anime using multiple recommendation techniques and displays anime posters using the Jikan API.

## Live Demo

🔗 **Deployed Application**
https://animerecommender-48vcz3ilp4qrkgilaxpsij.streamlit.app/

---

## Project Overview

This project implements three recommendation approaches:

* Content-Based Filtering
* Collaborative Filtering (KNN)
* Hybrid Recommendation System

The application allows users to select an anime and receive recommendations using different recommendation strategies.

Anime posters are fetched dynamically using the Jikan API and displayed through an interactive Streamlit web application.

---

## Features

* Content-Based Recommendation System
* Collaborative Filtering using KNN
* Hybrid Recommendation System
* Anime Poster Integration using Jikan API
* Interactive Streamlit Interface
* Cloud Deployment using Streamlit Community Cloud

---

## Recommendation Techniques

### 1. Content-Based Filtering

Content-Based Filtering recommends anime based on genre similarity.

#### Technologies Used

* CountVectorizer
* Cosine Similarity
* Feature Engineering

#### Working

Genres are converted into numerical vectors using CountVectorizer.

Example:

```text
Death Note
→ Mystery, Psychological, Supernatural
```

Anime with similar genre vectors receive higher similarity scores and are recommended to the user.

---

### 2. Collaborative Filtering

Collaborative Filtering recommends anime based on user rating behavior.

#### Technologies Used

* User-Anime Rating Matrix
* Sparse Matrix Representation
* K-Nearest Neighbors (KNN)
* Cosine Distance

#### Working

Users who rate anime similarly are grouped together.

Example:

```text
Users who liked Death Note
also liked Monster
```

Recommendations are generated based on rating patterns instead of anime genres.

#### Dataset Optimization

To reduce model size and enable deployment:

* Inactive users were removed.
* Anime with very few ratings were removed.
* The pivot table was rebuilt using the filtered dataset.

This significantly reduced memory usage while maintaining useful recommendations for popular anime.

#### Note

Collaborative Filtering is available only for anime present in the filtered dataset.

If an anime does not have sufficient rating data, the application displays a message and users can still use the Content-Based Recommender.

---

### 3. Hybrid Recommendation System

The Hybrid Recommendation System combines:

* Content-Based Recommendations
* Collaborative Filtering Recommendations

This helps improve recommendation diversity and overall recommendation quality.

---

## Dataset

Files Used:

* anime.csv
* rating.csv

The dataset contains:

* Anime Information
* Genres
* User Ratings
* Anime Ratings
* User Interactions

---

## Technologies Used

### Machine Learning

* Scikit-Learn
* K-Nearest Neighbors (KNN)
* CountVectorizer
* Cosine Similarity

### Data Processing

* Pandas
* NumPy
* SciPy

### Web Application

* Streamlit

### API Integration

* Jikan API

### Version Control

* Git
* GitHub

### Deployment

* Streamlit Community Cloud

---

## Project Structure

```text
anime_recommender/
│
├── app.py
├── requirements.txt
├── README.md
│
└── model/
    ├── anime.pkl
    ├── vectors.pkl
    ├── pivot_table.pkl
    └── knn_model_df.pkl
```

---

## Optimization Performed

### Content-Based Optimization

Initially, the project stored a complete similarity matrix.

```python
similarity = cosine_similarity(vectors)
```

This produced a very large file because similarities between every pair of anime were stored.

Optimization:

* Stored vectors instead of the complete similarity matrix.
* Calculated cosine similarity dynamically during runtime.
* Reduced storage requirements significantly.
* Maintained recommendation quality.

### Collaborative Filtering Optimization

The original pivot table contained a very large number of users and anime.

Optimization:

* Filtered inactive users.
* Filtered anime with low interaction counts.
* Reduced pivot table size.
* Reduced model storage requirements.

### Deployment Optimization

Model files were optimized to reduce storage usage and improve deployment performance.

Final model files:

* anime.pkl
* vectors.pkl
* pivot_table.pkl
* knn_model_df.pkl

---

## Challenges Faced

### Large Model Files

The original similarity matrix occupied hundreds of megabytes.

Solution:

* Replaced similarity matrix storage with vector storage.
* Generated similarity scores dynamically when recommendations are requested.

### DataFrame Index Mismatch

An indexing issue occurred because DataFrame indices did not align with similarity matrix rows.

Solution:

```python
anime_df = anime_df.reset_index(drop=True)
```

This ensured that anime indices matched the corresponding vector positions.

### Deployment Constraints

Large model files made deployment difficult.

Solution:

* Optimized datasets.
* Reduced model size.
* Filtered low-interaction records.
* Used runtime similarity calculations.

---

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/Tushar-Dhakrey/anime_recommender.git
```

Move into the project directory:

```bash
cd anime_recommender
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Skills Demonstrated

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Content-Based Recommendation Systems
* Collaborative Filtering
* Hybrid Recommendation Systems
* API Integration
* Streamlit Development
* Git & GitHub
* Model Optimization
* Cloud Deployment
* Debugging & Problem Solving

---

## Future Scope

Potential improvements include:

* Personalized user accounts
* User authentication
* Advanced recommendation ranking
* Deep Learning-based recommendation models
* User watchlist functionality

---

## Author

**Tushar Dhakrey**

GitHub: https://github.com/Tushar-Dhakrey

LinkedIn: Add Your LinkedIn Profile Here
