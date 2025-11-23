import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=45.4794&longitude=8.6982&current_weather=true"

response = requests.get(url)

status = response.status_code

print(f"Status: {status}")

data = response.json()

print(data)