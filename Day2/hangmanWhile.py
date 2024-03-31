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

# use a while loop so your game keeps going till the word has been guessed
trials = 0
game_over = False
while not game_over:
    guess = input("Guess a Letter: ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        trials += 1
        guesses_left = 5 - trials
        print(f"You have {guesses_left} more trials")
        if trials >= 5:
            print("You Lose")
            game_over = True
    print(display_word)
    if "_" not in display_word:
        print("You Win")
        game_over = True
