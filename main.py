import requests
import time
import random
from PIL import Image
from functions import *

icon = "Icon1.png"

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

            invia_notifica("Task da Fare", f"Task: {message} \nCompletion status: {completion}", icon)
    except:
        print("Connection to API failed")
    
    time.sleep(15)