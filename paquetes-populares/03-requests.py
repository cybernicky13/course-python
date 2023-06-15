import requests

# url = "https://jsonplaceholder.typicode.com/users"

# r = requests.get(url, timeout=10)
# print(
#     r.status_code,
#     r.text
#     )

# r = r.json()
# for user in r:
#     print(user["name"])

# url = "https://jsonplaceholder.typicode.com/users/1"
# r = requests.get(url, timeout=10)
# print(r.json())

# url = "https://jsonplaceholder.typicode.com/users"
# user = {
#     "name": "Guts"
# }
# r = requests.post(url, timeout=10, data=user)
# print(r.status_code)

# url = "https://jsonplaceholder.typicode.com/users/13"
# user = {
#     "name": "Guts"
# }
# r = requests.put(url, timeout=10, data=user)
# print(r.status_code)

# url = "https://jsonplaceholder.typicode.com/users/13"
# r = requests.delete(url, timeout=10)
# print(r.status_code)

url = "https://jsonplaceholder.typicode.com/users/13"
apikey = "1234567890"
headers = {
    "Authorization": f"Bearer {apikey}"
}

r = requests.delete(url, timeout=10, headers=headers)
print(r.status_code)