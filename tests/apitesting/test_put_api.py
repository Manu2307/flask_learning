import requests

put_url = 'http://127.0.0.1:5000/learning/update'

payload_data = {
    "email": "manojkumar.andrapu@gmail.com",
    "skill_name": "API Testing 5",
    "duration": 1.5,
    "learning_resource": "Digital-Learning"
}


def test_put_api():
    record_id = '0487c2dd-6680-42f5-b3f9-51637f34a24c'
    response = requests.put(put_url + f'/{record_id}', json=payload_data)
    data = response.json()
    assert response.status_code == 200

    assert data["data"]["email"] == payload_data['email']
    assert data["data"]["skill_name"] == payload_data['skill_name']
    assert data["data"]["duration"] == payload_data['duration']
    assert data["data"]["learning_resource"] == "Digital-Learning"
    assert response.headers['Content-Type'] == "application/json"

