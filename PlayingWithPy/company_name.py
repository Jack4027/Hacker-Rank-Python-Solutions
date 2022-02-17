#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    letters = set(s)
    counts = []
    for letter in letters:
        letterCount = s.count(letter)
        counts.append([letter,letterCount])
    
    counts = sorted(counts)
    counts = sorted(counts, key = lambda x: x[1], reverse = True )
    
    for i in range(3):
        print(counts[i][0]+' '+str(counts[i][1]))