#!/usr/bin/env python

def smorse_ray(fileName):
    with open(fileName) as f:
        data = f.readline().split() 
    return data

def smorse(strToMorse):
    data = smorse_ray('morse.txt')
    morsed = ""
    for letter in strToMorse:
        morsed += data[ord(letter) - 97]
    return morsed

print(smorse("sos"))
