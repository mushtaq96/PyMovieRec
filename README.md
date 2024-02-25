# Movie Recommendation System

## Overview
This project implements a movie recommendation system using precomputed similarity data and the TMDb API. The system generates personalized movie recommendations based on a user-selected movie. It is implemented in Python, utilizing Pandas for data manipulation and Streamlit for the web application.

## Data
The recommendation system relies on two precomputed data files:
- `movie_list.pkl`: Contains information about movies, including title, genres, keywords, cast, and crew.
- `similarity.pkl`: Stores precomputed similarity scores between movies.

## Implementation
### Data Preprocessing
The `movie_recommendation.ipynb` notebook contains code for data preprocessing. It loads data from `tmdb_5000_credits.csv` and `tmdb_5000_movies.csv`, merges them, cleans and transforms the data, and generates the `movie_list.pkl` and `similarity.pkl` files.

### User Interface
The `app.py` file contains code for the Streamlit app providing the user interface. Users can select a movie from a dropdown list or type in a moive name and receive recommendations, along with movie posters fetched from the TMDb API.

## Usage
To run the Streamlit app locally:
1. Install dependencies: `pip install -r requirements.txt`
2. Set up your TMDb API key by creating a `.env` file in the root directory with the following content: `TMDB_API_KEY=your_api_key_here`
3. Run the app: `streamlit run app.py`

## Example Usage

### Titanic Recommendation
![Titanic Recommendation](/images/titanic_recommendation.png)

In this screenshot, the user has entered "Titanic" as the selected movie. The application has responded with a list of recommended movies tailored to the user's input.

### Jurassic World Recommendation
![Jurassic World Recommendation](/images/jurassic_world_recommendation.png)

This screenshot demonstrates the movie recommendation system in action. The user has selected "Jurassic World" from the dropdown menu, and the application has provided a list of recommended movies based on this selection.

## Future Enhancements
- Incorporate machine learning techniques for recommendation, such as collaborative or content-based filtering.
- Explore the use of deep learning to improve recommendation quality.
- Enhance user interface with more interactive features and better visualization.

## Contributing
Contributions to this project are welcome! If you have suggestions for improvements or find any issues, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
