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

print(smorse("sos"))
