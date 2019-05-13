#!/usr/bin/python3

# Author: Daniel Harvey
# Written: April 9 2018

import random

# Generate the random integer between 5 and 15, inclusive
numToGuess = round(random.random() * 10) + 5

guess = int(input("Guess the integer between 5 and 15: "))

guessCounter = 1
while guess != numToGuess :
	diff = abs(guess - numToGuess)
	if diff < 3 :
		print("HOT")
	else:
		print("COLD")

	guessCounter += 1
	guess = int(input("Guess the integer between 5 and 15: "))

else:
	print("MATCH")
	print("You took %d guesses." %  (guessCounter))

print(numToGuess)
