#!/usr/bin/python3

#Author: Daniel Harvey
#Written: April 25, 2018

import random, hmload, hmvars, hmround

def grabWord():
    if len(dictWords) > 0:
        return str(random.choice(list(dictWords.keys())))
    else:
        return None

dictWords = hmload.loadDictionary()
#print(dictWords)

while hmvars.playerScore < hmvars.maxScore and hmvars.playerScore > hmvars.minScore:
    word = grabWord()
    
    if word is not None:
        winner = hmround.playRound(word)
        
        print()
        if winner:
            print("Congratulations!  You win this round.")
            hmvars.playerScore += dictWords[word]
        else:
            print("Better luck next time.")
            hmvars.playerScore -= dictWords[word]

        print("Your current score is %d points.\n" % (hmvars.playerScore))
        del dictWords[word]
    else:
        print("\nNo words left to play. Your final score is %d\n" % (hmvars.playerScore))
        quit()
    
   
else:
    if hmvars.playerScore >= hmvars.maxScore:
        print("You win!")
    elif hmvars.playerScore <= hmvars.minScore:
        print("You lose!")
