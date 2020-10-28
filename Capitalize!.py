#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    sa=""
    #Method_2
    sa+=s[0].upper()
    for i in range(1,len(s)):
        if s[i]==" ":
            sa+=s[i]
        elif s[i-1]==" ":
            if s[i]==" ":
                sa+=s[i]
            else:
                sa+=s[i].upper()
        else:
            sa+=s[i]
    return sa


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
