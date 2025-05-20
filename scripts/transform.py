# transform.py
import pandas as pd
import sqlite3

conn = sqlite3.connect("db/weather.db")
df = pd.read_sql("SELECT * FROM weather_raw", conn)

df["temp_celsius"] = df["temp"] - 273.15
df["date"] = pd.to_datetime(df["timestamp"]).dt.date

df_cleaned = df[["city", "temp_celsius", "humidity", "date"]]
df_cleaned.to_sql("weather_cleaned", conn, if_exists="replace", index=False)
df_cleaned.to_csv("data/cleaned_weather_data.csv", index=False)

conn.close()
print("✅ Data cleaned and stored.")
