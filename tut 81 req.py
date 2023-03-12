import requests
r=requests.get("https://fakestoreapi.com/products/1")
print(r.json())
print(r.status_code)