# python_hangman
From: https://medium.com/@andrewyang96/coding-a-game-of-hangman-in-python-from-scratch-a538542e5c0c

The prompt is below:
Ask for number of attempts, make sure it is between 1 and 25, inclusive
Ask for minimum word length, make sure it is between 4 and 16, inclusive [I will explain this later.]
Open the word list file & select a random word
Create a set of remaining letters and initialize it to contain the 26 ASCII lowercase character
While there are attempts remaining OR there are unguessed letters in the word remaining
    Print the word with the unguessed letters censored
    Ask for the next letter and make it lowercase
    If the "letter" has multiple characters
        Notify the player that the "letter" has multiple characters
    Else if the letter is not an ASCII lowercase character
        Notify the player that the letter is not an ASCII lowercase character
    Else if the letter is not in the remaining letter set (i.e. has been guessed before)
        Notify the player that the letter has been guessed before
    Else
        If letter is in the word
            Notify the player that the letter is in the word
        Else
            Decrement attempt counter
            Notify the player that the letter is not in the word
        Remove guessed letter from the remaining letter set
Reveal the word
If the word is solved
    Notify the player of victory
Else
    Notify the player of defeat
Give the player the option to try again


#if variable instead of if variable is true; python if boolean vs if boolean = true
#pieces of program pulled out and call when you need it
#create array and operator that creates 
