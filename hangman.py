import random
import string

# Ask for number of attempts, make sure it is between 1 and 25, inclusive
triesValid = False
while triesValid is False:
    print("How many tries would you like to guess the word? Pick a number from 1 to 25.")
    tries = input()
    # Convert to int and validate number
    tries = int(tries)
    if tries >= 1 and tries <= 25:
        triesValid = True
        continue
    else:
        triesValid = False

# Ask for minimum word length, make sure it is between 4 and 16, inclusive [I will explain this later.]
lengthValid = False
while lengthValid is False:
    print("How long would you like your word to be? Pick a number from 4 to 16.")
    length = input()
    # Convert to int to validate number
    length = int(length)
    if length >= 4 and length <= 16:
        lengthValid = True
        continue
    else:
        lengthValid = False

# Open the word list file & select a random word
# fileOpen = open("C:\Users\ellie\OneDrive\Documents\Programming Practice\wordListUse.txt", "r")
wordListUse = open("wordListUse.txt", "r").readlines()
# use the length variable and random to find a word that is the right length
# select that word and set it to the variable secretWord
secretWord = 0
while secretWord == "0":
    i = random.randint(0, 69321)
    if len(wordListUse[i]) == length:
        secretWord == wordListUse[i]

# Create a set of remaining letters and initialize it to contain the 26 ASCII lowercase character
lowerAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
remainingLettersSet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                       "t", "u", "v", "w", "x", "y", "z"]

# Where my loop begins...
# While there are attempts remaining OR there are unguessed letters in the word remaining
# Print the word with the unguessed letters censored
gameContinues = True
roundContinues = True
while roundContinues is True:
    print("Please guess a letter.")
    for j in range(len(secretWord)):
        if secretWord[j] in remainingLettersSet:
            print(" _ ")
        else:
            print(secretWord[j])
    # Ask for the next letter and make it lowercase
    guessedLetter = input()
    lowerGuess = string.lower(guessedLetter)
    # If the "letter" has multiple characters Notify the player that the "letter" has multiple characters
    if len(lowerGuess) > 1:
        print("Please guess only one letter at a time.")
    # Else if the letter is not an ASCII lowercase character Notify the player that the letter is not an ASCII
    # lowercase character
    elif lowerGuess not in lowerAlphabet:
        print("Please guess a letter.")
    # Else if the letter is not in the remaining letter set (i.e. has been guessed before) Notify the player that the
    # letter has been guessed before
    elif lowerGuess not in remainingLettersSet:
        print("You have already guessed that letter. Please guess another letter.")
    # Else If letter is in the word Notify the player that the letter is in the word
    elif lowerGuess in secretWord:
        remainingLettersSet.remove(lowerGuess)
        print("That is correct! You have ", tries, " tries left.")
    # Else Decrement attempt counter Notify the player that the letter is not in the word
    # Remove guessed letter from the remaining letter set
    else:
        remainingLettersSet.remove(lowerGuess)
        tries = tries - 1
        print("That is incorrect. You have ", tries, " tries left.")
    if tries == 0:
        roundContinues = False

    for k in range(len(secretWord)):
        if secretWord[k] in remainingLettersSet:
            continue
        else:
            roundContinues = False

    # Reveal the word If the word is solved Notify the player of victory
    print("The secret word was ", secretWord, ".")
    # Else Notify the player of defeat
    if tries != 0:
        print("You won!")
    else:
        print("You lost!")

    # Give the player the option to try again
    questionLoop = True
    continueGame = 0
    while questionLoop is True:
        print("Would you like to try again? Y/N")
        continueGame = input()
        if continueGame == "Y":
            gameContinues = True
            questionLoop = False
        elif continueGame == "N":
            print("Thank you for playing.")
            gameContinues = False
            questionLoop = False
        else:
            continue
