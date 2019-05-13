# Author: Daniel Harvey
# Written: April 25 2018

dictFileName = "dictionary.txt"

def loadDictionary():
    try:
        dictionaryText = open(dictFileName,'r').read()
        
        wordsAndScores = {}
        for line in dictionaryText.split('\n'):
            pair = line.split()
            if len(pair) == 2:
                wordsAndScores.update({str(pair[0]): int(pair[1])});
        
        return wordsAndScores

    except FileNotFoundError:
        print("Could not open file \'" + dictFileName + '\'')
        return None


