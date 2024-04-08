import random
import string

try:
    alphabet = list(string.punctuation + string.digits + string.ascii_letters)

    passwordLength = int(input("Pass Length(8-16): "))
    if 16 >= passwordLength >= 8:
        password = input("Anything you want included in your passphrase: ")
        if len(password) < passwordLength:
            diff = passwordLength - len(password)
            for i in range(0, diff):
                filler = random.choice(alphabet)
                password = filler + password
            passFile = open("Password.txt", "a")
            print(password)
            passFile.write(f"\nYour Password: {password}")
            print(f"Get your password from {passFile}")
            passFile.close()

    else:
        print("Choose a length from 8 to 16 characters")
except ValueError:
    print("Use Numerical values(0-9)")
    
