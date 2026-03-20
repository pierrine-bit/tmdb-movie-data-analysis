import requests
from config import API_KEY, BASE_URL


# -----------------------------------------------------------
# Fetch movie details
# -----------------------------------------------------------

def get_movie(movie_id):
    # build endpoint URL
    url = f"{BASE_URL}/{movie_id}"

    try:
        # send request to TMDB API
        response = requests.get(
            url,
            params={"api_key": API_KEY},
            timeout=10
        )

        print(f"[GET MOVIE] {movie_id} → Status {response.status_code}")

        # raise error if request failed
        response.raise_for_status()

        data = response.json()

        # check if API returned an error message
        if isinstance(data, dict) and data.get("success") is False:
            print(f"API error for movie {movie_id}: {data}")
            return None

        return data

    except requests.exceptions.RequestException as e:
        # handle request issues (timeout, connection error, etc.)
        print(f"Request failed for movie {movie_id}: {e}")
        return None


# -----------------------------------------------------------
# Fetch movie credits (cast + crew)
# -----------------------------------------------------------

def get_credits(movie_id):
    # build endpoint URL for credits
    url = f"{BASE_URL}/{movie_id}/credits"

    try:
        # send request to TMDB API
        response = requests.get(
            url,
            params={"api_key": API_KEY},
            timeout=10
        )

        print(f"[GET CREDITS] {movie_id} → Status {response.status_code}")

        # raise error if request failed
        response.raise_for_status()

        data = response.json()

        # check if API returned an error message
        if isinstance(data, dict) and data.get("success") is False:
            print(f"API error for credits {movie_id}: {data}")
            return None

        return data

    except requests.exceptions.RequestException as e:
        # handle request issues
        print(f"Request failed for credits {movie_id}: {e}")
        return None