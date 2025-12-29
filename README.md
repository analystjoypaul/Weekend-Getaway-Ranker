# Weekend Getaway Ranker

A **Streamlit-based travel recommendation system** that ranks the **top weekend destinations** for any Indian city using ratings, popularity, visit time, and entry cost. Ideal for travelers looking for quick weekend trips without spending hours researching.

---

## Project Overview

Weekend trips are great, but choosing the best places nearby can be overwhelming.  
The **Weekend Getaway Ranker** simplifies this by providing **automated rankings** of destinations based on:

- Tourist ratings  
- Popularity (number of Google reviews)  
- Time required to visit  
- Free or paid entry  

The user selects a **source city**, and the app generates the **Top 5 weekend destinations** with detailed insights.

---

## Live Demo

> Add a link here if deployed on Streamlit Cloud or your server.  
> Example: [Live Demo](https://your-streamlit-app-link)

---

## Features

- ✅ **City-based destination ranking**
- ⭐ **Rating normalization** for fair comparison
- 📈 **Popularity scoring** based on Google reviews
- ⏱️ **Time suitability** scoring (shorter trips score higher)
- 💰 **Free-entry bonus**
- ⚡ **Fast performance** using Streamlit caching
- 📋 **Interactive data table** display
- 🔢 **Weighted scoring system** for overall ranking

---

## 🛠️ Tech Stack

- **Python 3.x**  
- **Pandas** – Data manipulation & feature engineering  
- **Streamlit** – Interactive web app  
- **CSV Dataset** – `Top Indian Places to Visit.csv`  

---

## 📂 Dataset

The dataset includes Indian tourist destinations with the following relevant columns:

| Column | Description |
|--------|-------------|
| City | Source city |
| Name | Destination name |
| Type | Place type (Temple, Hill Station, Historical, etc.) |
| Google review rating | Avg. rating from Google |
| Number of google review in lakhs | Popularity indicator |
| time needed to visit in hrs | Hours required to explore |
| Entrance Fee in INR | Cost of entry |

> The dataset CSV is included in the repo: `Top Indian Places to Visit.csv`

---

## 🧠 Ranking Logic

Each destination is scored using **normalized and weighted factors**:

| Factor | Weight |
|--------|--------|
| Google Rating | 40% |
| Popularity (Reviews) | 30% |
| Time Suitability | 20% |
| Free Entry Bonus | 10% |

**Formula:**

```text
final_score =
0.4 × rating_norm +
0.3 × popularity_norm +
0.2 × time_score +
0.1 × entry_bonus
