import pandas as pd
import numpy as np


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform cleaned movie DataFrame into analysis-ready dataset.

    Responsibilities:
    - Convert data types
    - Handle missing / invalid values
    - Create financial KPIs
    - Filter valid movies
    - Enforce data quality
    - Return structured dataset for analysis
    """

    df = df.copy()

    # ------------------------------------------------------------------
    # 1. Convert numeric columns safely
    # ------------------------------------------------------------------
    numeric_cols = [
        'budget', 'revenue', 'runtime',
        'popularity', 'vote_count', 'vote_average'
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        else:
            df[col] = np.nan

    # ------------------------------------------------------------------
    # 2. Convert date column
    # ------------------------------------------------------------------
    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    else:
        df["release_date"] = pd.NaT

    # ------------------------------------------------------------------
    # 3. Replace invalid zero values
    # ------------------------------------------------------------------
    for col in ["budget", "revenue", "runtime"]:
        if col in df.columns:
            df.loc[df[col] == 0, col] = np.nan

    # ------------------------------------------------------------------
    # 4. Create financial features (in millions USD)
    # ------------------------------------------------------------------
    df["budget_musd"] = df["budget"] / 1_000_000
    df["revenue_musd"] = df["revenue"] / 1_000_000

    # Profit
    df["profit_musd"] = df["revenue_musd"] - df["budget_musd"]

    # ROI (handle division safely)
    df["roi"] = np.where(
        df["budget_musd"] > 0,
        df["revenue_musd"] / df["budget_musd"],
        np.nan
    )

    # ------------------------------------------------------------------
    # 5. Keep only released movies
    # ------------------------------------------------------------------
    if "status" in df.columns:
        df = df[df["status"] == "Released"]
        df = df.drop(columns=["status"], errors="ignore")

    # ------------------------------------------------------------------
    # 6. Convert lists to strings (avoid duplicate errors)
    # ------------------------------------------------------------------
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: str(x) if isinstance(x, list) else x
        )

    # ------------------------------------------------------------------
    # 7. Remove duplicates
    # ------------------------------------------------------------------
    if "id" in df.columns:
        df = df.drop_duplicates(subset=["id"])
    else:
        df = df.drop_duplicates()

    # ------------------------------------------------------------------
    # 8. Remove rows missing critical fields
    # ------------------------------------------------------------------
    df = df.dropna(subset=["id", "title"])

    # ------------------------------------------------------------------
    # 9. Enforce minimum data completeness
    # ------------------------------------------------------------------
    df = df.dropna(thresh=10)

    # ------------------------------------------------------------------
    # 10. Reset index
    # ------------------------------------------------------------------
    df = df.reset_index(drop=True)

    # ------------------------------------------------------------------
    # 11. Final column selection (FIXED)
    # ------------------------------------------------------------------
    final_cols = [
        'id', 'title', 'tagline', 'release_date', 'genres',
        'belongs_to_collection', 'original_language',

        #  Financial metrics (FIXED)
        'budget_musd',
        'revenue_musd',
        'profit_musd',
        'roi',

        'production_companies',
        'production_countries',
        'vote_count',
        'vote_average',
        'popularity',
        'runtime',
        'overview',
        'spoken_languages',
        'poster_path',

        # Credits
        'cast',
        'cast_size',
        'director',
        'crew_size'
    ]

    # Keep only existing columns (safe selection)
    final_cols = [col for col in final_cols if col in df.columns]

    df = df[final_cols]

    # ------------------------------------------------------------------
    # DEBUG (optional but useful)
    # ------------------------------------------------------------------
    print("\n Final dataset shape:", df.shape)
    print(" Final columns:", df.columns.tolist())

    return df