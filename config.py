import os


# -----------------------------------------------------------
# API configuration
# -----------------------------------------------------------

# base endpoint for movie API
BASE_URL = "https://api.themoviedb.org/3/movie"

# API key (used to authenticate requests)
API_KEY = "1a66cf9f283cad8d30e13096de0af285"



# -----------------------------------------------------------
# Input data
# -----------------------------------------------------------

# list of movie IDs used for data collection
MOVIE_IDS = [
    299534, 19995, 140607, 299536, 597, 135397, 420818,
    24428, 168259, 99861, 284054, 12445, 181808, 330457,
    351286, 109445, 321612, 260513
]


# -----------------------------------------------------------
# Pipeline settings
# -----------------------------------------------------------

# number of parallel requests
MAX_WORKERS = 8

# output file for cleaned dataset
OUTPUT_FILE = "data/movies_clean.csv"