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

# Returns a dictionary with each unique smorsed string as a key and the value being number of occurrences
def number_of_occurrences(dataList):
    morseDict = {}
    for item in dataList:
        if item not in morseDict:
            morseDict[item] = 1
        else:
            morseDict[item] += 1
    return morseDict

print(number_of_occurrences(file_smorse('tiny.txt')))
