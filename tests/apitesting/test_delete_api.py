import requests

url = "http://127.0.0.1:5000/learning"


def test_get_all_api():
    record_id = '0487c2dd-6680-42f5-b3f9-51637f34a245c'
    get_response = requests.get(url + f'/get/{record_id}')
    get_data = get_response.json()
    delete_response = requests.delete(url + f'/delete/{record_id}')
    delete_data = delete_response.json()



    assert

    assert response.status_code == 202

