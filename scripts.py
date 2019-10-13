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

## Ex 2 - List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = [ [i,j,k] 
        for i in range (x+1) 
        for j in range (y+1) 
        for k in range (z+1) 
        if i+j+k!=n #constraints
        ]
    print( list )

## Ex 3 - Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    # create the array for the scores
    scores = list(map(int, input().split()))
    # get the max
    m = max(scores)
    # store the temporary min (algo for min)
    minScore = min(scores)
    for x in scores:
        if(x>minScore and x<m):
            minScore = x
    print(minScore)

## Ex 4 - Nested Lists

if __name__ == '__main__':
    # get the number of students
    studentsNumber = int(int(input()))
    # grade and students for each student
    gradeStudents = [[input(),float(input())] for i in range(0 , studentsNumber)]
    # list of grades
    grades = []
    for grade in gradeStudents: grades.append(grade[1])
    # Create a set of grades and find the min
    setGrades = set(grades)
    setGrades.remove(min(setGrades))   
    # Compute the second lowest grade
    minGrade = min(setGrades)
    # Get the students name 
    minStudents = [s[0] for s in gradeStudents if s[1] == minGrade]
    # sort the set
    sortedStudents = sorted(minStudents)
    # print the students
    for s in sortedStudents:
        print(s)

## Ex 5 - Finding the percentage

if __name__ == '__main__':
    n = int(input())o
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # compute the mean
    average = sum(student_marks[query_name])/3
    # format the mean
    print("%.2f" % average)

## Ex 6 - Lists

List = []
result = []
N = int(input())
for i in range(N):
    List = input().split()
    if List[0] == "insert" :
        position = int(List[1])
        integer = int(List[2])
        result.insert(position,integer)
    if List[0] == "remove" :
        rem_int = int(List[1])
        result.remove(rem_int)
    if List[0] == "append" :
        append_int = int(List[1])
        result.append(append_int)
    if List[0] == "sort" :
        result.sort()
    if List[0] == "pop" :
        result.pop()
    if List[0] == "reverse" :
        result.reverse()
    if List[0] == "print" :
        print(result)

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

