# scripts/etl.py
import subprocess

print("🔄 Starting ETL pipeline...")

# Step 1: Fetch data from OpenWeatherMap API
subprocess.run(["python", "scripts/fetch_data.py"], check=True)

# Step 2: Load raw data into SQLite
subprocess.run(["python", "scripts/load_to_db.py"], check=True)

# Step 3: Transform and clean the data
subprocess.run(["python", "scripts/transform.py"], check=True)

print("✅ ETL pipeline completed successfully.")
