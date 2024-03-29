# "Guess the Number"
# Programmed by Zachary Fruhling
# Copyright 2020

import random

correctAnswer = random.randint(1, 100)
gameOver = False

while gameOver == False:

    playerGuess = int(input("Guess a number between 1 and 100: "))

    if playerGuess == correctAnswer:
        compareAnswer = "Right"
        gameOver = True
    elif playerGuess > correctAnswer:
        compareAnswer = "High"
    elif playerGuess < correctAnswer:
        compareAnswer = "Low"

    if compareAnswer == "Right":
        print("Correct! You Win!")
    elif compareAnswer == "High":
        print("Too High! Guess Again!")
    elif compareAnswer == "Low":
        print("Too Low! Guess Again!")

()