

# TMDB Movie Data Analysis

## 1. Introduction

This report presents the results of analyzing movie performance using data collected from the TMDB API.
The goal is to understand how movies perform financially, how efficiently they use their budgets, and how audiences respond to them.

---

## 2. Data Source

The dataset was obtained from the TMDB API and includes:

* Financial data (budget, revenue)
* Audience metrics (ratings, votes, popularity)
* Movie metadata (genres, collections, cast, directors)

The analysis is based on a selected set of popular movies.

---

## 3. Methodology

The data was processed through a pipeline involving cleaning, transformation, and feature engineering.
Key variables such as **profit** and **ROI** were derived and used to compare movie performance across different dimensions.

---

## 4. Results and Interpretation

### Top Revenue and Profit

From the ranking tables, *Avatar* clearly stands out as the top-performing movie, generating over **2900 million USD** in revenue and the highest profit in the dataset.

What is interesting is that the top revenue and top profit rankings are almost identical. Movies like *Avengers: Endgame* and *Titanic* consistently appear at the top in both cases. This suggests that high revenue in this dataset generally translates directly into high profit, meaning production costs are effectively recovered.

However, when looking at the lower end of profit, movies such as *Star Wars: The Last Jedi* still appear profitable but rank lower compared to others. This shows that even high-budget blockbusters can be less efficient relative to their scale.

---

### Return on Investment (ROI)

ROI provides a different perspective from revenue.

*Avatar* again ranks first, but what stands out is that movies like *Jurassic World* and *Harry Potter and the Deathly Hallows: Part 2* also perform very strongly despite not being the absolute highest in revenue.

This highlights an important point:
 **High revenue does not always mean high efficiency.**

Movies with moderate budgets can achieve very strong ROI, making them more efficient investments. On the other hand, movies like *Star Wars: The Last Jedi* have lower ROI, indicating that their high budgets reduce their relative efficiency.

---

### Budget vs Revenue

The revenue vs budget plot shows a clear upward trend, confirming that higher budgets are generally associated with higher revenues.

However, the spread of the data points is quite wide. Some movies with similar budgets produce very different revenues. This suggests that while budget is important, it is not the only factor influencing success.

In other words, spending more increases potential, but does not guarantee success.

---

### Audience Engagement

From the tables, *The Avengers* has the highest number of votes, making it the most engaged movie in the dataset.

At the same time, *Avengers: Endgame* and *Avengers: Infinity War* have the highest ratings. This shows that some movies manage to achieve both strong popularity and high audience satisfaction.

However, there are also cases where movies generate high revenue but receive relatively lower ratings. This indicates that:

**Commercial success and audience perception do not always align.**

---

### Franchise vs Standalone Performance

The franchise analysis provides one of the most interesting insights.

From the aggregated results:

* Franchise movies have **higher average budgets**
* They generate **stable but slightly lower ROI compared to standalone movies**
* Standalone movies show **higher ROI on average**

This suggests that:

 Franchises are **lower-risk investments**, offering consistent performance
 Standalone movies are **higher-risk but potentially higher-reward**

This difference reflects two strategies in the movie industry:

* Franchise-based stability
* Standalone innovation and variability

---

### Most Successful Franchises

Looking at the franchise ranking table, **The Avengers Collection** dominates in terms of total revenue.

Other franchises such as *Star Wars* and *Jurassic Park* also perform strongly, but not at the same level.

An important observation here is that:

Success is not just about one movie, but about **consistent performance across multiple releases**

Franchises benefit from brand recognition and audience loyalty, which helps sustain high revenue over time.

---

### Most Successful Directors

Director analysis shows that **James Cameron** leads in total revenue, largely driven by highly successful films like *Avatar* and *Titanic*.

Other directors such as *Joss Whedon* and the *Russo brothers* also rank highly due to their involvement in major franchise films.

This indicates that:

Directors play a key role, but their success is often linked to **large-scale productions and strong franchises**

---

### Revenue Trends Over Time

Revenue trends fluctuate rather than follow a steady pattern. Peaks in revenue correspond to the release of major blockbuster movies.

This suggests that:

The industry is heavily influenced by **individual high-performing films**, rather than consistent yearly growth.

---

## 5. Key Observations

* High revenue often leads to high profit, but not necessarily high efficiency
* ROI highlights efficient movies that may not have the highest revenue
* Budget is important but not sufficient to guarantee success
* Popularity and ratings measure different aspects of audience response
* Franchise movies offer stability, while standalone movies offer variability
* A small number of franchises and directors dominate overall performance

---

## 6. Limitations

* The dataset includes only a limited number of selected movies
* Results are not representative of the entire movie industry
* Some queries return empty results due to missing data
* External factors such as inflation are not considered

---

## 7. Challenges

* Handling nested JSON data required careful transformation
* Some API responses were incomplete or inconsistent
* Ensuring consistency across multiple pipeline stages
* Debugging data flow and validating outputs

---

## 8. Conclusion

This analysis shows that movie performance is influenced by both scale and efficiency.

While large budgets often drive high revenue, ROI provides a more meaningful measure of performance. Franchise movies tend to provide stability, while standalone movies offer greater variability and potential upside.

Overall, the pipeline successfully transforms raw API data into structured insights, allowing for a deeper understanding of how movies perform across different dimensions.

---
