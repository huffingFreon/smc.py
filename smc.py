#!/usr/bin/env python

def smorse_dict(fileName):
    with open(fileName) as f:
        data = [x.split() for x in f]
    print(data)

def smorse(strToMorse):
    smorse_dict('morse.txt')

smorse(2)
