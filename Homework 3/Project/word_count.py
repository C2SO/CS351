
from mrjob.job import MRJob
from mrjob.step import MRStep
from itertools import tee
import re
import sys

WORD_KEY = re.compile(r"[\w']+")

# New class for MRJob Word Probability
class MapReduce(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.input_file),
            MRStep(mapper=self.set_bigrams,
                   reducer=self.count_bigrams),
            MRStep(reducer=self.solution)
        ]
    
    # Step 1 - Edits the file's lines to make them more "readable"
    def input_file(self, _, line):
        if(line[0] != '"'):
            yield (None, line[line.find(","):].lower())
    
    # Step 2 - Pull words from the string and make a bigram for every word
    def set_bigrams(self, _, line):
        prev = ""
        # Find all the words
        for word in WORD_KEY.findall(line):
            if(prev != ""):
                yield ((prev, word), 1)
            prev = word
    
    # Step 2 - Combine all like bigrams
    def count_bigrams(self, word, counts):
        first_word, second_word = word
        yield first_word, (sum(counts), second_word)
        
    # Function used to sort by probability
    def mostUsed(self, x):
        num, word = x
        return num
    
    # Step 3 - Calculate percentages
    def solution(self, word, pairs):
        total = 0
        
        # Tee off the iterator so we can have 3 total runs through the data
        pairs, secondPairs = tee(pairs)
        pairs, secondPairs = tee(pairs)
        
        # First, calculate the total number of occurences of each bigram
        for pair in pairs:
            tempCount, _ = pair
            total = total + tempCount
        
        # Second, create and print the probability list
        probabilityList = sorted(secondPairs, key=self.mostUsed, reverse = True)
        for tempPair in probabilityList:
            word_count, word_key = tempPair
            yield (word, word_key), ((float(word_count) / total), word_count)
        
        # Third, if the first word is "my", print the most used pairs
        if (word == "my"):
            for i in range(10):
                if i == len(probabilityList): 
                    break
                word_count, word_key = probabilityList[i]
                yield 'Most Used - ' + str(i+1), ((word, word_key), word_count / total, word_count)
        
        # Third, if the first word is "my", print the most used pairs
        if (word == "my"):
            for i in range(10):
                if i == len(probabilityList): 
                    break
                word_count, word_key = probabilityList[i]
                yield 'Most Used - ' + str(i+1), ((word, word_key), word_count / total, word_count)
        
        

# Run the program
if __name__ == '__main__':
    MapReduce.run()
