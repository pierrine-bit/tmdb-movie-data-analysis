# -----------------------------------------------------------
# Rank movies based on a selected metric
# -----------------------------------------------------------

def rank_movies(df, metric, n=10, ascending=False):
    """
    Sort dataset by a given metric and return top results.
    """

    return (
        df.sort_values(metric, ascending=ascending)
        [["title", metric]]
        .head(n)
    )


# -----------------------------------------------------------
# Franchise vs Standalone analysis
# -----------------------------------------------------------

def franchise_analysis(df):
    """
    Compare franchise and standalone movies using key metrics.
    """

    temp = df.copy()
    temp["is_franchise"] = temp["belongs_to_collection"].notna()

    return temp.groupby("is_franchise").agg({
        "revenue_musd": "mean",
        "roi": "median",
        "budget_musd": "mean",
        "popularity": "mean",
        "vote_average": "mean"
    }).round(2)


# -----------------------------------------------------------
# Most successful franchises
# -----------------------------------------------------------

def top_franchises(df, n=10):
    """
    Identify most successful franchises based on revenue and size.
    """

    temp = df[df["belongs_to_collection"].notna()]

    result = (
        temp.groupby("belongs_to_collection")
        .agg(
            num_movies=("id", "count"),
            total_budget=("budget_musd", "sum"),
            avg_budget=("budget_musd", "mean"),
            total_revenue=("revenue_musd", "sum"),
            avg_revenue=("revenue_musd", "mean"),
            avg_rating=("vote_average", "mean")
        )
        .sort_values("total_revenue", ascending=False)
        .head(n)
    )

    return result.round(2)


# -----------------------------------------------------------
# Most successful directors
# -----------------------------------------------------------

def top_directors(df, n=10):
    """
    Identify top directors based on total revenue and ratings.
    """

    temp = df[df["director"].notna()]

    result = (
        temp.groupby("director")
        .agg(
            num_movies=("id", "count"),
            total_revenue=("revenue_musd", "sum"),
            avg_rating=("vote_average", "mean")
        )
        .sort_values("total_revenue", ascending=False)
        .head(n)
    )

    return result.round(2)


# -----------------------------------------------------------
# Compute all KPIs
# -----------------------------------------------------------

def all_kpis(df):
    """
    Generate all KPIs including rankings and advanced analysis.
    """

    roi_df = df[df["budget_musd"] >= 10]

    return {

        # ------------------------------
        # Basic rankings
        # ------------------------------
        "TOP_REVENUE": rank_movies(df, "revenue_musd"),
        "TOP_BUDGET": rank_movies(df, "budget_musd"),

        "TOP_PROFIT": rank_movies(df, "profit_musd"),
        "LOW_PROFIT": rank_movies(df, "profit_musd", ascending=True),

        "TOP_ROI": rank_movies(roi_df, "roi"),
        "LOW_ROI": rank_movies(roi_df, "roi", ascending=True),

        "MOST_VOTED": rank_movies(df, "vote_count"),

        "TOP_RATED": rank_movies(df[df.vote_count >= 10], "vote_average"),
        "LOW_RATED": rank_movies(df[df.vote_count >= 10], "vote_average", ascending=True),

        "MOST_POPULAR": rank_movies(df, "popularity"),

        # ------------------------------
        # Advanced analysis (NEW)
        # ------------------------------
        "FRANCHISE_ANALYSIS": franchise_analysis(df),
        "TOP_FRANCHISES": top_franchises(df),
        "TOP_DIRECTORS": top_directors(df),
    }