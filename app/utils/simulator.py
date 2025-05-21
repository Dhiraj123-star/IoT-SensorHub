import requests
from datetime import datetime,timezone
import random
import time
from requests.exceptions import RequestException
from time import sleep


def send_data():
    data = {
        "device_id": "sensor-1",
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "pressure": round(random.uniform(980, 1050), 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    retries = 3
    for attempt in range(retries):
        try:
            res = requests.post("http://localhost:8000/ingest", json=data, timeout=5)
            print("Response:", res.json())
            return
        except RequestException as e:
            print(f"Error (attempt {attempt + 1}/{retries}): {e}")
            if attempt < retries - 1:
                sleep(2 ** attempt)  # Exponential backoff
            else:
                print("Max retries reached, skipping...")

while True:
    send_data()
    time.sleep(5)




