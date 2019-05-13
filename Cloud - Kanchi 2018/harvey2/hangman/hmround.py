# Author: Daniel Harvey
# Written: April 25 2018

maxGuesses = 6

def printGuessData(word, lettersGuessed, numberOfGuesses):
    currentGuess = ""
    for char in word:
        if lettersGuessed.count(char) == 0:
            currentGuess += "- "
        else:
            currentGuess += char + " "
    
    usedLetters = ""
    for char in lettersGuessed:
        usedLetters += char + ' '
    
    print("\nCurrent Guess: %s\nUsed Letters: %s\nNumber of tries left: %d\n"
          % (currentGuess.strip(), usedLetters.strip(), maxGuesses - numberOfGuesses))
    return

def checkWin(word, lettersGuessed):
    "If all the letters in the word have been guessed, return true.  Otherwise return False."
    for char in word:
        if lettersGuessed.count(char) == 0:
            return False
    return True

def playRound(word):
    "Returns True if player wins, False is player loses the round"
    
    numberOfGuesses = 0
    lettersGuessed  = []
    wordGuessed = False

    print("I have picked a word.  Please guess letters of the word.  You will have %d incorrect tries allowed." % (maxGuesses))

    while numberOfGuesses < maxGuesses:
        #print the stuff for each guess
        printGuessData(word, lettersGuessed, numberOfGuesses)
        
        guess = str(input("Guess a letter or the whole word: ")).lower()
        numberOfGuesses += 1

        if len(guess) > 1: # the whole word was guessed
            if guess == word:
                print("You guessed the word!")
                return True
            else:
                print("Sorry that is not the word.")
        elif len(guess) == 1: # only one letter guessed
            lettersGuessed.append(guess)

            if word.find(guess) == -1:
                print("Sorry no %s." % (guess))
            else:
                print("Yes there is a %s." % (guess))
                wordGuessed = checkWin(word, lettersGuessed)
                if wordGuessed:
                    break
        else: # blank guess? shouldn't count as a guess
            numberOfGuesses -= 1




    print("\nThe correct word was %s.\n" % (word))
    return wordGuessed
        

