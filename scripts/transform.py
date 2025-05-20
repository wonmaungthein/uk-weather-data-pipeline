# scripts/transform.py
import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("db/weather.db")

# Load raw data from the database
df = pd.read_sql("SELECT * FROM weather_raw", conn)

# Convert temperature from Kelvin to Celsius
df["temp_celsius"] = df["temp"] - 273.15

# Extract just the date (no time) from the timestamp
df["date"] = pd.to_datetime(df["timestamp"]).dt.date

# Create a cleaned version of the DataFrame
df_cleaned = df[["city", "temp_celsius", "humidity", "date"]]

# Save cleaned data to new table and CSV
df_cleaned.to_sql("weather_cleaned", conn, if_exists="replace", index=False)
df_cleaned.to_csv("data/cleaned_weather_data.csv", index=False)

# Close the connection
conn.close()

print("✅ Data transformed and saved.")
