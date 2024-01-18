import requests

url = "http://127.0.0.1:5000/learning/create"

request_data = {
    "associate_id": "6edb2671-a5e0-4e29-b287-623ca5472084",
    "email": "manojkumar.andhrapu@senecaglobal.com",
    "skill_name": "API Testing",
    "duration": 9.5,
    "learning_resource": "E-Learning",
    "resource_link": "E-Learning",
    "start_datetime": "2023-11-26 21:35:00",
    "end_datetime": "2023-12-26 21:35:00",
    "status": "started"
}

response = requests.post(url, json=request_data)

response_data = response.json()

assert response.status_code == 201

assert response_data["data"]["skill_name"] == "API Testing"
