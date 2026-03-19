import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# set simple consistent style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


# ---------------------------------------------------------------
# Revenue vs Budget
# ---------------------------------------------------------------

def revenue_vs_budget(df):
    """
    Show relationship between budget and revenue.
    """

    if "budget_musd" not in df or "revenue_musd" not in df:
        print("Missing budget or revenue column")
        return

    plt.figure()
    sns.regplot(data=df, x="budget_musd", y="revenue_musd")

    plt.title("Revenue vs Budget")
    plt.xlabel("Budget (Million USD)")
    plt.ylabel("Revenue (Million USD)")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------
# Popularity vs Rating
# ---------------------------------------------------------------

def popularity_vs_rating(df):
    """
    Compare popularity with rating.
    """

    if "popularity" not in df or "vote_average" not in df:
        print("Missing popularity or rating column")
        return

    plt.figure()
    sns.scatterplot(data=df, x="vote_average", y="popularity")

    plt.title("Popularity vs Rating")
    plt.xlabel("Rating")
    plt.ylabel("Popularity")

    plt.tight_layout()
    plt.show()

# -----------------------------------------------------------
# ROI distribution by genre
# -----------------------------------------------------------

def roi_distribution(df: pd.DataFrame, show: bool = False) -> None:

    # check required columns
    required_cols = ["genres", "roi"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # prepare data
    data = df.copy()
    data = data.dropna(subset=["genres", "roi"])

    # split multiple genres into rows
    data["genres"] = data["genres"].str.split("|")
    data = data.explode("genres")

    # plot
    plt.figure()
    sns.boxplot(data=data, x="genres", y="roi")

    plt.xticks(rotation=45)
    plt.title("ROI Distribution by Genre")
    plt.xlabel("Genre")
    plt.ylabel("ROI")
    plt.tight_layout()
    plt.show()

    # save plot
    #_save_plot("roi_distribution.png", show)

# ---------------------------------------------------------------
# Yearly Revenue Trend
# ---------------------------------------------------------------

def yearly_trends(df):
    """
    Show how revenue changes over time.
    """

    if "release_date" not in df or "revenue_musd" not in df:
        print("Missing release_date or revenue")
        return

    temp = df.copy()
    temp["year"] = temp["release_date"].dt.year

    yearly = (
        temp.groupby("year")["revenue_musd"]
        .sum()
        .reset_index()
        .sort_values("year")
    )

    plt.figure()
    sns.lineplot(data=yearly, x="year", y="revenue_musd")

    plt.title("Yearly Revenue Trend")
    plt.xlabel("Year")
    plt.ylabel("Revenue (Million USD)")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------
# Franchise vs Standalone
# ---------------------------------------------------------------

def franchise_vs_standalone(df):
    """
    Compare revenue for franchise vs standalone movies.
    """

    if "belongs_to_collection" not in df:
        print("Collection column missing")
        return

    temp = df.copy()
    temp["franchise"] = temp["belongs_to_collection"].notna()

    plt.figure()
    sns.boxplot(data=temp, x="franchise", y="revenue_musd")

    plt.title("Franchise vs Standalone")
    plt.xlabel("Is Franchise")
    plt.ylabel("Revenue (Million USD)")

    plt.tight_layout()
    plt.show()