import requests

url = "http://127.0.0.1:5000/learning/get"


def test_get_all_api():
    record_id = '0487c2dd-6680-42f5-b3f9-51637f34a245c'
    response = requests.get(url + f'/{record_id}')
    record_data = response.json()

    if record_data["message"]:
        assert response.status_code == 500
        assert record_data["message"] == "An unexpected error has occurred."
        assert record_data["status"] == "error"
    else:
        data = record_data["data"]
        assert response.status_code == 200
        assert 'associate_id' in data
        assert 'email' in data
        assert 'skill_name' in data
        assert 'duration' in data
        assert 'learning_resource' in data
        assert 'resource_link' in data
        assert 'status' in data
        assert response.headers['Content-Type'] == "application/json"




