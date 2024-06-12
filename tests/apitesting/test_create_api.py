import requests

create_url = "http://127.0.0.1:5000/learning/create"
get_url = "http://127.0.0.1:5000/learning/get"

payload = {
    "associate_id": "6edb2671-a5e0-4e29-b287-623ca5472084",
    "email": "manojkumar.andhrapu@senecaglobal.com",
    "skill_name": "API Testing",
    "duration": 9.5,
    "learning_resource": "E-Learning",
    "resource_link": "E-Learning.com",
    "start_datetime": "2024-01-01 21:35:00",
    "end_datetime": "2024-01-19 21:35:00",
    "status": "started"
}


def test_create_api():
    create_response = requests.post(create_url, json=payload)
    create_response_data = create_response.json()

    assert create_response.status_code == 201
    record_id = create_response_data["data"]["id"]

    get_response = requests.get(get_url + f"/{record_id}")
    get_response_data = get_response.json()

    assert get_response.status_code == 200
    assert get_response_data["data"]["associate_id"] == payload["associate_id"]
    assert get_response_data["data"]["email"] == payload["email"]
    assert get_response_data["data"]["skill_name"] == payload["skill_name"]
    assert get_response_data["data"]["duration"] == payload["duration"]
    assert get_response_data["data"]["learning_resource"] == payload["learning_resource"]
    assert get_response_data["data"]["resource_link"] == payload["resource_link"]
    # assert response_data["data"]["start_datetime"] == "2024-01-01 21:35:00"
    # assert response_data["data"]["end_datetime"] == "2024-01-19 21:35:00"
    assert get_response_data["data"]["status"] == payload["status"]

    assert create_response.headers['Content-Type'] == "application/json"
