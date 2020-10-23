#!/bin/python3

import math
import os
import random
import re
import sys
n = int(input().strip())

if n%2==1:
    print("Weird")
elif n%2==0 and (n>= 2 and n<6):
    print("Not Weird")
elif n%2==0 and (n>6 and n<21):
    print("Weird")
else:
    print("Not Weird")
