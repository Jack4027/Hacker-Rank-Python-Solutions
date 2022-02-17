#!/bin/python3

import math
import os
import random
import re
import sys
import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    time1 = dt.datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z" )
    time2 = dt.datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z" )
    if time1>time2:
        difference = time1-time2
    else:
        difference = time2-time1
    return str(round(difference.total_seconds()))
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
