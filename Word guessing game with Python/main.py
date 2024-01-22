# In this game, there is a list of words present, out of which our interpreter will choose 1 random word. The user first has to input their names and then, will be asked to guess any alphabet. If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. The user will be given 12 turns(which can be changed accordingly) to guess the complete word.


import random
import requests

# Get the words list
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)

# Define a byte string, Words are in byte format!
byte_string = response.content.split()

# Select a random word
byte_word = random.choice(byte_string)

# Convert the byte string to a string
WORD = byte_word.decode("utf-8")

# print the word
print(WORD)

turns = len(WORD) + 5

def has_no_repeated_chars(string):
    for char in string:
        if string.count(char) > 1:
            pass
        else:
            return string
        
word = has_no_repeated_chars(WORD)
print(word)

user_name = input("Your name: ")

print(f"\n{user_name} you have {turns} choices Good luck!")

dashes = ""
for i in range(1, len(WORD) + 1):
    dashes = dashes + "_"

print(f"Guess the word {dashes}\n")


while turns > 0:
    user_guess = input("Guess a character: ")

    if user_guess in WORD and user_guess != "":
        word_index = WORD.index(user_guess)
        charList = list(dashes)
        charList[word_index] = user_guess
        dashes = "".join(charList)

    elif user_guess not in WORD:
        if turns == 0:
            print("You Loose!")
            break

        turns -= 1
        print("Wrong, You have", turns, "more guesses\n")


    print(dashes,"\n")
    

    if "_" not in dashes:
        print("Congratulations you win!")