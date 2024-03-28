# create a greeting
# create your wordlist
# randomly choose a word from the list
# ask the user to guess a letter
# bonus make the program take the input form the user and make it lowercase
# check if the letter is in the word
import time
import random

print("Welcome")
wordlist = ["Kali", "Linux", "Ubuntu", "Fedora", "Mint", "Debian"]
word = random.choice(wordlist)
guess = input("Guess a Letter: ").lower()

print("Scanning...")
time.sleep(4)
for letter in word:
    if letter == guess:
        print(f"{letter} Match")
    else:
        print(f"{letter} Wrong")
print(f"The word was {word}")


