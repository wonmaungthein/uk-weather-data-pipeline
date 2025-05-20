# fetch_data.py (updated)
import requests
import pandas as pd
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
cities = ["London", "Manchester", "Birmingham", "Leeds", "Glasgow", "Liverpool", "Bristol", "Sheffield", "Edinburgh", "Cardiff"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        flat_data = {
            "city": city,
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "timestamp": datetime.utcnow()
        }
        return flat_data
    else:
        print(f"Failed for {city}")
        return None

weather_data = []
for city in cities:
    result = fetch_weather(city)
    if result:
        weather_data.append(result)
    time.sleep(1)

df = pd.DataFrame(weather_data)
df.to_csv("data/raw_weather_data.csv", index=False)
print("✅ Weather data fetched and saved.")
