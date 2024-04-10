import requests

response = requests.post("https://httpbin.org/post", data={'love': 'isReal'})
