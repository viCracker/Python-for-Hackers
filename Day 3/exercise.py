# mosh exercise
import time

print("Welcome to Weight Conversion by viCracker")

weight = int(input("Weight: "))
type = input("(K)g or (L)bs: ").lower()

if type == "k":
    weight = round(weight * 2.205, 1)
    print("Converting...")
    time.sleep(3)
    print(f"Weight in Lbs: {weight}")
elif type == "l":
    weight = round(weight / 2.205, 1)
    print("Converting...")
    time.sleep(3)
    print(f"Weight in Kg: {weight}")
else:
    print("Try again with L(lbs) or K(kgs)")
