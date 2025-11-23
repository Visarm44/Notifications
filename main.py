import requests
import time
import random
from PIL import Image
from functions import *
import os
import datetime

current_folder =os.path.dirname(os.path.abspath(__file__))

#icon_path = os.path.join(current_folder, "Icon1.png")

while True:
    url = "https://api.open-meteo.com/v1/forecast?latitude=45.4794&longitude=8.6982&current_weather=true"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            current_weather = data["current_weather"]

            temperature = current_weather["temperature"]
            weathercode = current_weather["weathercode"]

            if weathercode == 0:
                icon_path = os.path.join(current_folder, "clear-day.svg")
            elif weathercode in range(1, 4):
                icon_path = os.path.join(current_folder, "cloudy-2-day.svg")
            elif weathercode in range(45, 49):
                icon_path = os.path.join(current_folder, "fog.svg")
            elif weathercode in range(51, 58):
                icon_path = os.path.join(current_folder, "rainy-1-day.svg")
            elif weathercode in range(61, 68) or weathercode in range(80, 83):
                icon_path = os.path.join(current_folder, "rainy-3.svg")
            elif weathercode in range(71, 78) or weathercode in range(85, 87):
                icon_path = os.path.join(current_folder, "snowy-3.svg")
            elif weathercode in range(95, 100):
                icon_path = os.path.join(current_folder, "thunderstorms.svg")
            else:
                icon_path = os.path.join(current_folder, "Icon1.png")

            invia_notifica("Meteo Galliate", f"Ci sono {temperature}°C", icon_path)
    except Exception as e:
        current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error_message = f"[ERRORE] {now} - Connection to {url} failed. Dettaglio: {e}\n"
        with open("error_log.txt", "a") as f:
            f.write(error_message)
        
        print("Error logged")
    time.sleep(3600)