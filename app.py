import streamlit as st
import pandas as pd

# --------------------------------
# Page Config
# --------------------------------
st.set_page_config(
    page_title="Weekend Getaway Ranker",
    layout="wide"
)

# --------------------------------
# Load Data
# --------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Top Indian Places to Visit.csv")

df = load_data()

st.title("Weekend Getaway Ranker")
st.caption("Best weekend destinations ranked automatically based on city")

# --------------------------------
# Sidebar Input (ONLY CITY)
# --------------------------------
st.sidebar.header("Source")
source_city = st.sidebar.selectbox(
    "Select Source City",
    sorted(df["City"].unique())
)

# --------------------------------
# Ranking Logic
# --------------------------------
def rank_weekend_destinations(source_city):
    
    data = df[df["City"] == source_city].copy()

    if data.empty:
        return pd.DataFrame()

    # Normalize Rating
    data["rating_norm"] = (
        data["Google review rating"] /
        df["Google review rating"].max()
    )

    # Normalize Popularity
    data["popularity_norm"] = (
        data["Number of google review in lakhs"] /
        df["Number of google review in lakhs"].max()
    )

    # Time Suitability (lower time = better)
    data["time_score"] = 1 - (
        data["time needed to visit in hrs"] /
        df["time needed to visit in hrs"].max()
    )

    # Free Entry Bonus
    data["entry_bonus"] = data["Entrance Fee in INR"].apply(
        lambda x: 1 if x == 0 else 0
    )

    # Final Score
    data["final_score"] = (
        0.4 * data["rating_norm"] +
        0.3 * data["popularity_norm"] +
        0.2 * data["time_score"] +
        0.1 * data["entry_bonus"]
    )*100

    # Fixed Top 5
    return (
        data.sort_values("final_score", ascending=False)
        .head(5)
        [[
            "Name",
            "Type",
            "Google review rating",
            "Number of google review in lakhs",
            "time needed to visit in hrs",
            "Entrance Fee in INR",
            "final_score"
        ]]
    )

# --------------------------------
# Display Output
# --------------------------------
st.subheader(f"Top Weekend Places in {source_city}")

result = rank_weekend_destinations(source_city)

if result.empty:
    st.warning("No destinations found for this city.")
else:
    st.dataframe(result, use_container_width=True)

# --------------------------------
# Footer Insight
# --------------------------------
st.markdown("---")
st.caption(
    "Ranking based on Rating (40%), Popularity (30%), Time Suitability (20%), Free Entry (10%)"
)
