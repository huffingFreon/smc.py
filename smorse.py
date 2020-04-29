#!/usr/bin/env python

# Returns array of 26 morse code letters from the file
def smorse_ray(fileName):
    with open(fileName) as f:
        data = f.readline().split() 
    return data

# Returns the string passed converted into morse code with no spaces
def smorse(strToMorse):
    data = smorse_ray('morse.txt')
    morsed = ""
    for letter in strToMorse:
        morsed += data[ord(letter) - 97]
    return morsed

# Returns a list of each line in the file smorsed
def file_smorse(fileName):
    with open(fileName) as f:
        data = f.read().splitlines()
        morsed = []
        for line in data:
            morsed.append(smorse(line))
    return morsed

# Returns a dictionary with each unique sequence as a key and the value being number of occurrences
def number_of_occurrences(dataList):
    morseDict = {}
    for item in dataList:
        if item not in morseDict:
            morseDict[item] = 1
        else:
            morseDict[item] += 1
    return morseDict

# Returns the word which translates to have fifteen sequential dashes
def sequential_dashes(dataList):
    lineCount = -1
    lineNumber = 0
    fifteenDashes = "---------------"
    for item in dataList:
        lineCount += 1
        if item.count(fifteenDashes) == 1:
            lineNumber = lineCount
    with open('enable1.txt') as f:
        data = f.read().splitlines()
    return data[lineNumber]

# Returns the words in a file of a specified length that have the same number of . and - when translated
def find_balanced(fileName, length):
    blackjack = []
    balanced = []
    with open(fileName) as f:
        data = f.read().splitlines()
        for line in data:
            if len(line) == length:
                blackjack.append(line)
    for word in blackjack:
        smorsed = smorse(word)
        if smorsed.count(".") == smorsed.count("-"):
            balanced.append(word)
    return balanced

'''
# Bonus 1: finding the only sequence that is the code for 13 different words
enableDict = number_of_occurrences(file_smorse('enable1.txt'))

for strMorse, occ in enableDict.items():
    if occ == 13:
        print(strMorse)
'''

'''
# Bonus 2: finding the only word that contains 15 sequential dashes when translated
print(sequential_dashes(file_smorse('enable1.txt')))
'''

# Bonus 3: finding the two words that are 21 characters long and contain the same number of . and - when translated
print(find_balanced('enable1.txt', 21))


