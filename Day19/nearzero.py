import time
try:
    num = float(input("Enter Number: "))
    count = 1
    while num > 0:
        num = num/2
        time.sleep(1)
        print(f"{count}:{num}")
        count += 1
except TypeError:
    print("Enter a valid number")
