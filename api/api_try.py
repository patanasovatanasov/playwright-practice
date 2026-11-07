import requests

r = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = r.json()
print(r.status_code)
print(data['address'])
print(data['email'])

r = requests.get("https://jsonplaceholder.typicode.com/users/9999")
print(r.status_code)
data = r.json()
print(data)
print(requests.get("https://jsonplaceholder.typicode.com/users/").json())