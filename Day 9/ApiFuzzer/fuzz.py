import requests
import sys


#10.10.105.83
def loop():
    for word in sys.stdin:
        response = requests.get(url=f"http://10.10.105.83:5000/{word}")
        if response.status_code == 404:
            loop()
        else:
            print(word, response)
            data = response.json()
            print(data)


loop()
#go to terminal type "cat small.txt | python3 fuzz.py"
