import requests
from requests.auth import HTTPBasicAuth

response = requests.get(f"http://192.168.0.1")
# ,auth=HTTPBasicAuth(username="admin",password="admin")
print (response.status_code)
print("input" in response.text)
print (response.headers.get('WWW-Authenticate', None))
