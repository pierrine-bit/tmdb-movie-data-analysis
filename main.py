from src.utils import setup_logging
from src.data_fetcher import fetch_movies_parallel
from src.data_cleaning import clean_movies
from src.feature_engineering import engineer_features
from src.kpi_analysis import all_kpis
from src.visualization import (
    revenue_vs_budget,
    popularity_vs_rating,
    roi_distribution,
    yearly_trends,
    franchise_vs_standalone
)

from config import OUTPUT_FILE


def main():

    # setup logging to track pipeline steps
    logger = setup_logging()
    logger.info("Pipeline started")

    # -----------------------------------------------------------
    # fetch data from TMDB API
    # -----------------------------------------------------------
    results = fetch_movies_parallel()

    # -----------------------------------------------------------
    # clean and structure the raw data
    # -----------------------------------------------------------
    df = clean_movies(results)

    # -----------------------------------------------------------
    # create new features like profit and ROI
    # -----------------------------------------------------------
    df = engineer_features(df)

    # -----------------------------------------------------------
    # save final dataset to csv
    # -----------------------------------------------------------
    df.to_csv(OUTPUT_FILE, index=False)
    logger.info("Data saved")

    # -----------------------------------------------------------
    # compute and display KPIs
    # -----------------------------------------------------------
    kpis = all_kpis(df)

    for name, table in kpis.items():
        print(f"\n{name}\n")
        print(table)

    # -----------------------------------------------------------
    # simple filters for quick exploration
    # -----------------------------------------------------------
    print("\nBruce Willis Sci-Fi Action\n")
    print(df[
        (df.genres.str.contains("Science Fiction", na=False)) &
        (df.genres.str.contains("Action", na=False)) &
        (df.cast.str.contains("Bruce Willis", na=False))
    ].sort_values("vote_average", ascending=False))

    print("\nUma Thurman & Tarantino\n")
    print(df[
        (df.cast.str.contains("Uma Thurman", na=False)) &
        (df.director == "Quentin Tarantino")
    ].sort_values("runtime"))

    # -----------------------------------------------------------
    # visualize key relationships
    # -----------------------------------------------------------
    revenue_vs_budget(df)
    popularity_vs_rating(df)
    roi_distribution(df)
    yearly_trends(df)
    franchise_vs_standalone(df)

    logger.info("Pipeline completed")


if __name__ == "__main__":
    main()