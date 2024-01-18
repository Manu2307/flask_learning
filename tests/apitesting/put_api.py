import requests

get_url = 'http://127.0.0.1:5000/learning/get/c4d36ef3-e140-43b2-925f-5eeee4c470c6'

response = requests.get(get_url)

print(response.status_code)

print(response.json())

put_url = 'http://127.0.0.1:5000/learning/update/c4d36ef3-e140-43b2-925f-5eeee4c470c6'

payload_data = {
    "associate_id": "6edb2671-a5e0-4e29-b287-623ca5472084",
    "email": "manojkumar.andhrapu@senecaglobal.com",
    "skill_name": "API Testing 4",
    "duration": 9.5,
    "learning_resource": "E-Learning",
    "resource_link": "hsfjabwsjedfbokA",
    "start_datetime": "2023-11-26 21:35:00",
    "end_datetime": "2023-12-26 21:35:00",
    "status": "started"
}

response = requests.put(put_url, json=payload_data)

print(response.status_code)

print(response.json())
