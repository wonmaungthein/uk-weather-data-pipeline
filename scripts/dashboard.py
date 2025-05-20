# scripts/dashboard.py
import streamlit as st
import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned_weather_data.csv")

# Streamlit app layout
st.set_page_config(page_title="UK Weather Dashboard", layout="wide")
st.title("🌤️ UK Weather Dashboard")
st.markdown("Monitor temperature and humidity trends across UK cities.")

# Sidebar for city selection
cities = sorted(df["city"].unique())
selected_city = st.sidebar.selectbox("Select a city", cities)

# Filter data by selected city
city_data = df[df["city"] == selected_city]

# Show metrics
st.subheader(f"Weather Trends in {selected_city}")
col1, col2 = st.columns(2)
col1.metric("Latest Temperature (°C)", f"{city_data['temp_celsius'].iloc[-1]:.2f}")
col2.metric("Latest Humidity (%)", f"{city_data['humidity'].iloc[-1]}")

# Line chart
st.line_chart(
    city_data.set_index("date")[["temp_celsius", "humidity"]],
    use_container_width=True
)
