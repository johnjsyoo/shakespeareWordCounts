#!/usr/bin/env python

__author__ = 'John'

########################################################################################################################
### IMPORT
########################################################################################################################

from nltk.corpus import stopwords
from pattern.en import singularize

fileList = ['./macbeth.txt','./romeojuliet.txt']

########################################################################################################################
### CREATE A CHARACTER LIST
########################################################################################################################

def corpusBuilder(fileName):
    """
    Build a list a words from the book
    """
    with open(fileName,'r') as f:
        bookInfo = f.read()
        line = bookInfo.strip()
        bookWords = line.split()
    return bookWords

def characterBuilder(fileName):
    """
    Build a list of all the characters
    """
    characterList = []
    for word in corpusBuilder(fileName):
        if word[0].isupper() and word.endswith('.'):
            characterName = word.rsplit('.')
            if characterName[0].lower() not in characterList:
                characterList.append(characterName[0].lower())
            else:
                continue
    return characterList

########################################################################################################################
### RETURN LIST OF WORDS
########################################################################################################################

def wordListCleaner(fileName):
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
            wordList.append(word.lower())
        else:
            continue
    return wordList

def printWords(fileName):
    """
    Print the words and their counts
    """
    current_word    = None
    current_count   = 0
    wordDict        = {}

    wordList = wordListCleaner(fileName)
    wordList.sort()

    for word in wordList:
        if current_word == word:
            current_count += 1
        else:
            wordDict[current_word] = current_count
            current_count = 1
            current_word = word
    count = 0
    for w in sorted(wordDict, key=wordDict.get, reverse=True)[0:50]:
        count += 1
        print count, w, wordDict[w] ## Print top words and their counts

########################################################################################################################
### EXECUTE
########################################################################################################################

if __name__ == '__main__':
    print 'MACBETH WORD COUNTS'
    printWords(fileList[0])

    print ''

    print 'ROMEO AND JULIET WORD COUNTS'
    printWords(fileList[1])