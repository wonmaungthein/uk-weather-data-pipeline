# load_to_db.py
import pandas as pd
import sqlite3

df = pd.read_csv("data/raw_weather_data.csv")
conn = sqlite3.connect("db/weather.db")
df.to_sql("weather_raw", conn, if_exists="replace", index=False)
conn.close()
print("✅ Data loaded to SQLite database.")
