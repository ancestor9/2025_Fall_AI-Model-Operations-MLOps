import requests

r = requests.get('http://localhost:8000/hi')
print(r.json())


# r = requests.post('http://localhost:8000/hi', json={"who": "Alice"})
# print(r.json())

# import httpx
# r = httpx.get('http://localhost:8000')
# print(r.json())