import requests

username = "admin"
password = "admin"
base_url = "http://127.0.0.1:8000/api"


url = f"{base_url}/login"
my_headers = {}
my_payload = {
    "username": username,
    "password": password
}

my_response = requests.post(url, headers=my_headers, json=my_payload)

# respone_body = my_response.json()
