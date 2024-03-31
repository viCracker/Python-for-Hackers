import random

print("Welcome to Hangman")

words = ["hacker", "bounty", "random"]
# create an empty list
# For each letter in the secret_word add a "_" that will be printed to the console
# Example if the word is hacker "_","_","_","_","_","_"

secret_word = random.choice(words)
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

guess = input("Guess a Letter: ").lower()
# loop through each of the letters in the chosen word
# if the letter is in the word replace the "_" with the letter

for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == guess:
        display_word[position] = letter
print(display_word)
