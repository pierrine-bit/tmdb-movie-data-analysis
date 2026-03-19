from concurrent.futures import ThreadPoolExecutor, as_completed
from config import MOVIE_IDS, MAX_WORKERS
from src.api_client import get_movie, get_credits
from src.utils import setup_logging


# -----------------------------------------------------------
# setup logging
# -----------------------------------------------------------

logger = setup_logging()


# -----------------------------------------------------------
# fetch single movie (details + credits)
# -----------------------------------------------------------

def fetch_single_movie(movie_id):

    try:
        # fetch movie data and credits
        movie = get_movie(movie_id)
        credits = get_credits(movie_id)

        return {"movie": movie, "credits": credits}

    except Exception as e:
        # log any unexpected error
        logger.error(f"Error fetching movie {movie_id}: {e}")
        return None


# -----------------------------------------------------------
# fetch all movies using parallel execution
# -----------------------------------------------------------

def fetch_movies_parallel():

    results = []

    # use thread pool for faster API calls
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        # submit all tasks
        futures = {
            executor.submit(fetch_single_movie, mid): mid
            for mid in MOVIE_IDS
        }

        # collect results 
        for future in as_completed(futures):

            result = future.result()

            if result:
                results.append(result)

    logger.info(f"Fetched {len(results)} movies")

    return results