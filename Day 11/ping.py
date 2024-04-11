import time

import requests

target = input("Target: ")
response = requests.get(target)
statuscode = response.status_code
ping_count = int(input("Ping count: "))
while ping_count > 0:
    if statuscode == 200:
        print(f"Target {target} is Up")
    else:
        print(f"Target {target} is Down")
    time.sleep(1)
    ping_count -= 1
