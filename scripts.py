#### Problem 1 
### Introduction

## Ex 1 - Hello World

# store the string "Hello, World!" in a variable
hello = "Hello, World!"
# print the variable
print(hello)

## Ex 2 - If, Else

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

## Ex 3  - Aritm op

if __name__ == '__main__':
    a = int(input())
    b = int(input())
# sum
print(a + b)
# diff
print(a - b)
# product
print(a * b)


## Ex 4 - Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print (a // b)
print (a / b)

## Ex 5 - Loops
if __name__ == '__main__':
    n = int(input())
# constraints
if n >= 1 & n <= 20:
    #for loop
    for x in range (0, n):
        #exponential function
        print (x**2)

## Ex 6 - Function

def is_leap(year):
    leap = False

    # Verbose version
    # if year %400 == 0: leap = True
    # else:
    #     if ( year%4==0 and not year %100 == 0): leap = True
    #     else: leap = False
    
    # Short version
    if year %400 == 0 or ( year % 4 == 0 and not (year %100 == 0)): leap = True
    return leap

year = int(input())
print (is_leap(year))

## Ex 7 - Print Function

if __name__ == '__main__':
    n = int(input())

for i in range(n): 
    if (i !=0): print(i, end ="")
print(n)

### Data Types

## Ex 1 - Tuples

if __name__ == '__main__':
    # get it out of the way the first line
    n = int(input())
    # read the second line and split by whitespace
    line = input().split()
    # save to a list
    integer_list = map(int, line)
    # convert to a tuple of ints, which is hashable
    tp = tuple(integer_list)
    # print the hash
    print(hash(tp))

### Strings

### Sets

### Collections

### Date and Time

### Exceptions

### Built-ins

### Python Functionals

### Regex and Parsing challenges

### XML

### Closures and Decorations

### Numpy


# § Problem 2
# 

# Birthday Cake
# 

