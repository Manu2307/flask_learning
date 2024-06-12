import requests

url = "http://127.0.0.1:5000/learning/get/all"


def test_get_all_api():
    response = requests.get(url)
    data = response.json()
    if data["data"]:
        for record in data['data']:
            assert 'associate_id' in record
            assert 'email' in record
            assert 'skill_name' in record
            assert 'duration' in record
            assert 'learning_resource' in record
            assert 'resource_link' in record
            assert 'status' in record

    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"


