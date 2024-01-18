import requests


url = "http://127.0.0.1:5000/learning/get/all"

response = requests.get(url)

print(response.status_code)

assert response.status_code == 200
