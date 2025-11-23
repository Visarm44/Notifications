import requests
import time
import random
from PIL import Image
from functions import *
import os
import datetime

current_folder =os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(current_folder, "Icon1.png")

base_url = "https://jsonplaceholder.typicode.com/todos/"
while True:
    random_number = random.randint(1, 10)

    url = base_url + str(random_number)

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            message = data["title"]
            completion = data["completed"]

            invia_notifica("Task da Fare", f"Task: {message} \nCompletion status: {completion}", icon_path)
    except:
        time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        error_log = f"Connection to {url} failed at: {time}"
        with open("error_log.txt", "a") as f:
            txt.dump(error_log, f)
    
    time.sleep(15)