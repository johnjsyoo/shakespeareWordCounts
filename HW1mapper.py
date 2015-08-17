#!/usr/bin/env python

from nltk.corpus import stopwords
from pattern.en import singularize
from HW1reducer import corpusBuilder, characterBuilder

fileList = ['./macbeth.txt','./romeojuliet.txt']

########################################################################################################################
### RETURN LIST OF WORDS
########################################################################################################################

def wordListPrint(fileName):
    """
    Remove all character names, plurality, and stop words
    """
    wordList = []
    characterList = characterBuilder(fileName)
    swords = stopwords.words('english')
    for word in corpusBuilder(fileName):
        word = word.strip('.:,()?!;[]')
        singularize(word)
        if word.lower() not in characterList and word.lower() not in swords and len(word) > 1:
            print '%s\t%s' % (word.lower(),1)
        else:
            continue

########################################################################################################################
### EXECUTE
########################################################################################################################

if __name__ == '__main__':
    print 'Press ENTER for Macbeth words..'
    raw_input()
    wordListPrint(fileList[0])

    print ''

    print 'Press Enter for Romeo and Juliet words..'
    raw_input()
    wordListPrint(fileList[1])