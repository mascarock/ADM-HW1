#!/bin/python3

import math
import os
import random
import re
import sys


#get the input
if __name__ == '__main__':
    n = int(input().strip())

#store the output
output = ""

# using the remainder operator, if the remainder is zero, 
# the number is odd, otherwise even
if n % 2 != 0: output = 'Weird'

# number is odd
else:
    if n > 1 & n < 6: output = 'Not Weird'
    if n > 5 & n < 21: output = 'Weird'
    if n > 20: output = 'Not Weird'
print(output)
