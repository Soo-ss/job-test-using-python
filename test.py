import requests

res = requests.get(url="https://jsonplaceholder.typicode.com/users")

data = res.json()

name_list = []
for user in data:
    name_list.append(user["name"])

print(name_list)