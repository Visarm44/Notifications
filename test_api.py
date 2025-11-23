import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

status = response.status_code

print(f"Status: {status}")

data = response.json()

print(f"Titolo: {data["title"]}")
print(f"Completion: {data["completed"]}")