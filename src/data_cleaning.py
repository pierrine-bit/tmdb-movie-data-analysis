import pandas as pd
import numpy as np
from typing import List


# -------------------------------------------------------------------
# Utility Functions
# -------------------------------------------------------------------

def extract_names(col):
    """
    Convert list of dictionaries to pipe-separated string of names.
    Example:
    [{"id": 1, "name": "Action"}] → "Action"
    """
    if isinstance(col, list) and len(col) > 0:
        return "|".join([c.get("name", "") for c in col if "name" in c])
    return np.nan


def process_credits(credits_list: List[dict]) -> pd.DataFrame:
    """
    Extract cast, director, and crew info from credits API.
    """

    records = []

    for c in credits_list:

        movie_id = c.get("id")

        cast = [x.get("name") for x in c.get("cast", [])[:5]]

        crew = c.get("crew", [])

        director = next(
            (x.get("name") for x in crew if x.get("job") == "Director"),
            None
        )

        records.append({
            "id": movie_id,
            "cast": "|".join([c for c in cast if c]),
            "cast_size": len(c.get("cast", [])),
            "director": director,
            "crew_size": len(crew)
        })

    return pd.DataFrame(records)


# -------------------------------------------------------------------
# Main Cleaning Function
# -------------------------------------------------------------------

def clean_movies(results: List[dict]) -> pd.DataFrame:
    """
    Flatten nested JSON fields into a usable format.

    - Converts list-based fields (genres, companies, countries, languages)
      into pipe-separated strings
    - Extracts collection name from belongs_to_collection

    Returns a cleaned DataFrame ready for analysis.
    """

    # ------------------------------------------------------------------
    # 1. Filter valid API responses
    # ------------------------------------------------------------------
    movies = [
        r["movie"] for r in results
        if r and isinstance(r.get("movie"), dict) and "id" in r["movie"]
    ]

    credits = [
        r["credits"] for r in results
        if r and isinstance(r.get("credits"), dict) and "id" in r["credits"]
    ]

    print(f"Valid movies fetched: {len(movies)}")

    if len(movies) == 0:
        raise ValueError("No valid movie data fetched. Check API key or API responses.")

    # ------------------------------------------------------------------
    # 2. Normalize JSON → DataFrame
    # ------------------------------------------------------------------
    movies_df = pd.json_normalize(movies).copy()

    print("Columns:", movies_df.columns.tolist())  # debug

    # ------------------------------------------------------------------
    # 3. Drop irrelevant columns
    # ------------------------------------------------------------------
    drop_cols = [
        'adult', 'imdb_id', 'original_title',
        'video', 'homepage', 'backdrop_path'
    ]

    movies_df = movies_df.drop(columns=drop_cols, errors='ignore')

    # ------------------------------------------------------------------
    # 4. Flatten JSON columns
    # ------------------------------------------------------------------
    json_cols = [
        "genres",
        "production_companies",
        "production_countries",
        "spoken_languages"
    ]

    for col in json_cols:
        if col in movies_df.columns:
            movies_df[col] = movies_df[col].apply(extract_names)
        else:
            movies_df[col] = np.nan

    # ------------------------------------------------------------------
    # 5. Handle belongs_to_collection
    # ------------------------------------------------------------------
    if "belongs_to_collection.name" in movies_df.columns:
        movies_df["belongs_to_collection"] = movies_df["belongs_to_collection.name"]

    elif "belongs_to_collection" in movies_df.columns:
        movies_df["belongs_to_collection"] = movies_df["belongs_to_collection"].apply(
            lambda x: x.get("name") if isinstance(x, dict) else np.nan
        )
    else:
        movies_df["belongs_to_collection"] = np.nan

    # Drop redundant columns
    cols_to_drop = [
        "belongs_to_collection.id",
        "belongs_to_collection.name",
        "belongs_to_collection.poster_path",
        "belongs_to_collection.backdrop_path"
    ]

    movies_df = movies_df.drop(columns=cols_to_drop, errors="ignore")

    # ------------------------------------------------------------------
    # 6. Process credits and merge
    # ------------------------------------------------------------------
    credits_df = process_credits(credits)

    if "id" not in movies_df.columns:
        raise ValueError("Missing 'id' column. API data invalid.")

    df = movies_df.merge(credits_df, on="id", how="left")

    # ------------------------------------------------------------------
    # 7. Clean text placeholders
    # ------------------------------------------------------------------
    if "overview" in df.columns:
        df["overview"] = df["overview"].replace("", np.nan)

    if "tagline" in df.columns:
        df["tagline"] = df["tagline"].replace("", np.nan)

    # ------------------------------------------------------------------
    # 8. Final safety checks
    # ------------------------------------------------------------------

    # Convert lists/dicts to string before removing duplicates
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: str(x) if isinstance(x, (list, dict)) else x
        )

    # Remove duplicates safely
    df = df.drop_duplicates()

    # Remove rows missing key fields
    if "id" in df.columns:
        df = df.dropna(subset=["id", "title"])

    # Reset index
    df = df.reset_index(drop=True)

    # Debug output
    print("\nCleaned dataset shape:", df.shape)
    print("Cleaned columns:", df.columns.tolist())

    return df