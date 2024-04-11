import string
import time

print("FACEBOOK LOGIN")
time.sleep(2)
name = input("Enter Username: ")
password = input("Enter Password: ")
u = string.ascii_uppercase
l = string.ascii_lowercase
p = string.punctuation
d = string.digits
all_kinds = ["u", "l", "p", "d"]
kind = []


def append(word):
    kind.append(word)

def missing():
    if j == "u":
        print("Missing Uppercase", end="|")
    elif j == "p":
        print("Missing Special Character", end="|")
    elif j == "d":
        print("Missing digits", end="|")
    elif j == "l":
        print("Missing Lowercase", end="|")
    elif j == "u":
        print("Missing Uppercase", end="|")


for char in password:
    if char in l:
        append("l")
    elif char in p:
        append("p")
    elif char in d:
        append("d")
    elif char in l:
        append("l")
    elif char in u:
        append("u")
kind_final = []
for i in kind:
    if i not in kind_final:
        kind_final.append(i)
print(f"Password Has Types: {kind_final}")
for j in all_kinds:
    if j not in kind_final:
        missing()
print(" ")
print("Final Assessment")
print(f"Length of Password: {len(password)}")
if len(password) > 13 and len(kind_final) > 1:
    print("Your Password is STRONG")
elif 11 <= len(password) <= 13:
    if len(kind_final) > 1:
        print("Strong")
    else:
        print("Your Password is GOOD")
elif 8 <= len(password) <= 10:
    if 1 < len(kind_final) <= 2:
        print("Good")
    if len(kind_final) >= 3:
        print("Strong")
    else:
        print("Your password is Weak")
elif 1 <= len(password) <= 7:
    print("Your password is Very Weak")
else:
    print("????")
