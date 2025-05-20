# scripts/load_to_db.py
import pandas as pd
import sqlite3
import os

# Load CSV file
df = pd.read_csv("data/raw_weather_data.csv")

# Connect to (or create) SQLite database
os.makedirs("db", exist_ok=True)
conn = sqlite3.connect("db/weather.db")

# Load data into a table named weather_raw
df.to_sql("weather_raw", conn, if_exists="replace", index=False)

# Close the connection
conn.close()

print("✅ Data loaded to SQLite database.")
