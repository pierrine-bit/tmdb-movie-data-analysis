

#  TMDB Movie Data Analysis Pipeline

## An overview of the project

This project implements a data pipeline to collect, process, and analyze movie data from the TMDB (The Movie Database) API. The main goal is to transform raw JSON data into a structured dataset and generate meaningful insights about movie performance, including financial success, audience engagement, and investment efficiency.

The workflow follows a clear pipeline structure:

* Data extraction
* Data cleaning
* Feature engineering
* KPI analysis
* Visualization



## Objectives

* Fetch movie and credit data from the TMDB API
* Clean and structure nested JSON data
* Create financial metrics such as profit and ROI
* Analyze movie performance using ranking and aggregation
* Compare franchise vs standalone movies
* Identify the most successful franchises and directors
* Visualize key insights



## Data Source

Data is collected from the TMDB API and includes:

* Movie metadata (budget, revenue, popularity, etc.)
* Credits data (cast and crew, including directors)

A predefined list of movie IDs is used to ensure consistency and reproducibility.



## Project Structure

```
tmbd-movie-project/
│
├── data/
│   └── movies_clean.csv          
│
├── logs/
│   └── pipeline.log              
│
├── reports/
│   ├── analysis_summary.md       
│   └── figures/                  
│       ├── revenue_vs_budget.png
│       ├── popularity_vs_rating.png
│       ├── roi_distribution_by_genre.png
│       ├── franchise_vs_standalone.png
│       └── yearly_revenue_trend.png
│
├── src/
│   ├── api_client.py             
│   ├── data_fetcher.py           
│   ├── data_cleaning.py          
│   ├── feature_engineering.py    
│   ├── kpi_analysis.py           
│   ├── visualization.py          
│   ├── utils.py                  
│                 
├── main.py                       
├── config.py                     
└── README.md                     
```



## Methodology

### 1. Data Extraction

* Movie and credit data are fetched using the TMDB API
* Parallel processing is used to improve performance
* Basic error handling ensures stability



### 2. Data Cleaning

* Nested JSON fields are flattened (genres, companies, languages)
* Irrelevant columns are removed
* Missing and inconsistent values are handled
* Collection names and credits are extracted



### 3. Feature Engineering

New variables are created for analysis:

* `budget_musd` → budget in million USD
* `revenue_musd` → revenue in million USD
* `profit_musd` → revenue − budget
* `roi` → return on investment
Where the dataset is also filtered to keep only valid and released movies.



### 4. KPI Analysis

Movies are analyzed using different metrics:

* Highest revenue
* Highest budget
* Highest and lowest profit
* Highest and lowest ROI (budget ≥ 10M)
* Most voted movies
* Highest and lowest rated movies
* Most popular movies

Additional analysis includes:

* **Franchise vs standalone comparison**
* **Most successful franchises**
* **Most successful directors**



### 5. Visualization

The project includes the following visualizations:

* Revenue vs Budget
* ROI distribution by genre
* Popularity vs Rating
* Yearly revenue trends
* Franchise vs standalone comparison

All visual outputs are stored in:

```
reports/figures/
```



## Outputs

After running:

```bash
python main.py
```

The following are generated:

* Clean dataset → `data/movies_clean.csv`
* KPI tables (printed in terminal)
* Visualizations → `reports/figures/`
* Logs → `logs/pipeline.log`



## Key Insights

* Movies with higher budgets generally generate higher revenue
* ROI highlights efficiency rather than scale
* Some lower-budget movies achieve strong performance
* Popularity and rating are not always correlated
* Franchise movies show more consistent performance
* A few franchises dominate total revenue
* Certain directors (for instance James Cameron) contribute significantly to success



## Limitations

* The dataset includes only a small number of selected movies
* Results are not representative of the full movie industry
* Some filters return empty results due to dataset limitations
* External factors such as inflation are not considered



## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Seaborn



## How to Run the Project

### 1. Activate the virtual environment

```bash
.venv\Scripts\activate
```

### 2. Run the pipeline

```bash
python main.py
```

---
