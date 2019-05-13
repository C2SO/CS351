#!/usr/bin/python3

#Author: Daniel Harvey
#Written: April 25, 2018

inputText = input("Enter some text: ")

# Find the sum of all numbers in the string

sum = 0

for word in inputText.strip().split():
    if word.split('.')[0].isnumeric():
        sum += int(word.split('.')[0])

print("\"%s\", The sum of the numbers is %d." % (inputText, sum))

