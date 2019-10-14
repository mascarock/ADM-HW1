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
    n = int(input())
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

## Ex 1 - Swap Case

def swap_case(s):
    str = ""
    for i in range(len(s)):
        if s[i].islower():
            str += s[i].upper()
        else:
            str += s[i].lower()
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

## Ex 2 - Split and Join

def split_and_join(line):
    # line to split
    toSplit = line.split(" ")
    return "-".join(toSplit)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


## Ex 3 - What's your name?

def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

    
## Ex 4 - Mutations

def mutate_string(string, index, char):
    return string[:index] + char + string[index+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

## Ex 5 - Find a String

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if(sub_string[0]==string[i]):
            if(string[i:i+len(sub_string)]==sub_string):
                count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

## Ex 7 - String validation

if __name__ == '__main__':
    s = input()
    alphanum = False
    alpha = False
    dig = False
    lc = False
    uc = False
    for i in range(len(s)):
        if s[i].isalnum():
            alphanum = True
        if s[i].isalpha():
            alpha = True
        if s[i].isdigit():
            dig = True
        if s[i].islower():
            lc = True
        if s[i].isupper():
            uc = True
    print(alphanum)
    print(alpha)
    print(dig)
    print(lc)
    print(uc)

## Ex 8 - Text Alignment
thk = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thk):
    print((c*i).rjust(thk-1)+c+(c*i).ljust(thk-1))

#Top Pillars
for i in range(thk+1):
    print((c*thk).center(thk*2)+(c*thk).center(thk*6))

#Middle Belt
for i in range((thk+1)//2):
    print((c*thk*5).center(thk*6))

#Bottom Pillars
for i in range(thk+1):
    print((c*thk).center(thk*2)+(c*thk).center(thk*6))

#Bottom Cone
for i in range(thk):
    print(((c*(thk-i-1)).rjust(thk)+c+(c*(thk-i-1)).ljust(thk)).rjust(thk*6))

## Ex 9 - Text Alignment

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

## Ex 10 - Designer Door Mat

if __name__ == "__main__":
    # get the input
    n, m = map(int, input().split())
    central = ("WELCOME").center(m, "-")

    for i in range(n//2):
        print((".|."*(2*i+1)).center(m, "-"))

    print(central)

    for i in range((n//2)-1, -1, -1):
        print((".|."*(2*i+1)).center(m, "-"))

## Ex 11 - String Formatting

def print_formatted(number):
    w = len(bin(number))-2
    for i in range(1, number +1):
       print(("{0:"+ str(w) +"d} {1:"+ str(w) +"o} {2:"+ str(w) +"X} {3:"+ str(w) +"b}").format(i, i, i, i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

## Ex 12 - Alphabet Rangoli

import string

def print_rangoli(size):
    pattern = []
    size = int(size)
    for i in range(size):
        p = "-".join(string.ascii_lowercase[i:size])
        pattern.append((p[::-1] + p[1:]).center(4*size-3, "-"))
    
    # final pattern
    print("\n".join(pattern[:0:-1] + pattern))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

## Ex 13 -  Capitalize
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    bl = True
    for i in range(len(s)):
        if s[i] == ' ':
            bl = True
        elif bl == True:
            s = s[:i] + s[i].upper() + s[i+1:]
            bl = False
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

## Ex 14 - Minion Game

def minion_game(string):
    # your code goes here
    lst = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if lst.__contains__(s[i]):
            kevin += len(string) -i
        else:
            stuart += len(string) -i
    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif stuart < kevin:
        print("Kevin " + str(kevin))
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
## Ex 6 - Merge the Tools

def merge_the_tools(string, k):
    for i in range(len(string) // k):  # we should repeat the process len(string)/k times to reach all the string
        s = ""
        for j in string[i * k: i * k + k]:

            if j not in s:
                s += j
        print(s)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

### Sets

## Ex 1 - Intro

    # new function definition
    def average_(array):
    # your code goes here
        s = set(arr)
    # compute the average
        return sum(s)/len(s) 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average_(arr)
    print(result)


## Ex 2 - Sym diff.
if __name__ == '__main__':
    m = int(input())
    set1 = set(map(int, input().split()))
    n = int(input())
    set2 = set(map(int, input().split()))

    sd = set1.__xor__(set2)
    for i in range(len(sd)):
        print(min(sd))
        sd.remove(min(sd))

## Ex 3 - No Idea!

n , m = map(int, input().split())
L = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
antani = 0
for i in L :
    if i in A :
        antani += 1
    if i in B :
        antani -= 1
print(antani)

## Ex 4 - Set.add()

N = int(input())
# avoiding repeated values...
s = set()
for i in range(0,N) :
    s.add(input())

print(len(s))

## Ex 5 - Set .discard(), .remove() & .pop()
if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    nc = int(input())

    for i in range(nc):
        command = input().split()
        if command[0] == 'pop':
            s.pop()
        elif command[0] == 'remove':
            s.remove(int(command[1]))
        elif command[0] == 'discard':
            s.discard(int(command[1]))
    print(sum(s))

## Ex 6  - Set .union()

input()
en = set(map(int, input().split()))
input()
fr = set(map(int, input().split()))
print(len(en.union(fr)))

## Ex 7 -  Set .intersection()

input()
en = set(map(int, input().split()))
input()
fr = set(map(int, input().split()))
print(len(en.intersection(fr)))


## Ex 8 - Set .difference()

input()
en = set(map(int, input().split()))
input()
fr = set(map(int, input().split()))
print(len(en.difference(fr)))


## Ex 9 - Sym diff

input()
en = set(map(int, input().split()))
input()
fr = set(map(int, input().split()))
print(len(en.symmetric_difference(fr)))

## Ex 10 - Set Mutation

input()
a = set(map(int, input().split()))
for i in range(int(input())):
    command, n = input().split()
    s = set(map(int, input().split()))
    if command == "update":
        a.update(s)
    elif command == "intersection_update":
        a.intersection_update(s)
    elif command == "difference_update":
        a.difference_update(s)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(s)
print(sum(a))

## Ex 11 - The Captain's Room

k = int(input())
L = list(map(int, input().split()))
s = set(L)
print((sum(s)*k - sum(L))// (k-1))


## Ex 12 - Check subset

N = int(input())
for i in range(0, N):
    NA= int(input())
    A = set(map(int, input().split()))
    NB= int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))

## Ex 13 - check strict superset

A = set(map(int, input().split()))
N = int(input())
m = 1
for i in range(0, N):
    s = set(map(int, input().split()))
    if( s.issubset(A) == False) or  (len(A) - len(s) < 1) : # s should be a subset of A and A should have at least1 member more than s
        m *= 0
print(bool(m))


### Collections

## Ex 1 - Counter

X = int(input())
L = list(map(int, input().split()))
N = int(input())
money = 0
for i in range(0 , N) :
    customer = list(map(int, input().split()))
    if customer[0] in L :
        money += customer[1]
        L.remove(customer[0])
print(money)

## Ex 2 - DefaultDict

from collections import defaultdict
n, m = map(int, input().split())
a = defaultdict(list)
b = []
for i in range(n):
    a[input()].append(i+1)
for i in range(m):
    item = input()
    if a[item] == []:
        a[item].append(-1)
    print(" ".join(map(str,a[item])))

## Ex 3 - Namedtuple

from collections import namedtuple
sum = 0
N = int(input())
catg = input().split()
student_tup = namedtuple('student',catg)
for i in range(0, N):
    L = list(input().split())
    m = student_tup(L[0], L[1], L[2], L[3])
    sum += int(m.MARKS)

print(sum/N)

## Ex 4 - Word Order

from collections import OrderedDict
n = int(input())
od = OrderedDict()
for i in range(n):
    word = input()
    if od.__contains__(word):
        od[word] += 1
    else:
        od[word] = 1
print(len(od))
for item in od:
    print(od[item], end=" ")


## Ex 5 - Deque
from collections import deque

n = int(input())
d = deque()
for i in range(n):
    command = input().split()
    if command[0] == "append":
        d.append(int(command[1]))  
    elif command[0] == "appendleft":  
        d.appendleft(int(command[1]))  
    elif command[0] == "pop":
        d.pop()  
    elif command[0] == "popleft":
        d.popleft()
for i in d:
    print(i, end = " ")

## Ex 6 - Piling Up!
from collections import deque
t = int(input())
for i in range(t):
    d = deque()
    flag = True
    n = int(input())
    l = list(map(int, input().split()))
    for item in l:
        d.append(item)
    temp = 0
    if d[0] >= d[-1]:
        temp = d.popleft()
    else:
        temp = d.pop() 
    for k in range(n-2):
        if d[0] >= d[-1]:
            temp2 = d.popleft()
        else:
            temp2 = d.pop()
        if(temp < temp2):
            flag = False
        temp = temp2
    if d[0] <= temp and flag == True:
        print("Yes")
    else:
        print("No")
## Ex 7 - Logo

from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(s.replace(" ", ""))
    n = 3
    while n > 0:
        l = []
        m = max(c.values())
        for item in list(c):
            if c[item] == m:
                x = c.pop(item)
                l.append(item)
        l.sort()
        for i in l:
            if n > 0:
                print(str(i) + " " + str(m))
                n -= 1

# Ex 8 - Ordered 

if __name__ == '__main__':
    from collections import OrderedDict
    # Create new store Manager
    storeManager = OrderedDict()
    
    #get the number of items for dataentry
    nItems = int(input())

    for x in range(nItems):
        # separate the input in 3-tuple
        # skipping  the space
        item, space, quantity = input().rpartition(' ')

        #get the item and eventually update it
        storeManager[item] = storeManager.get(item, 0) + int(quantity)
    
    # print item and quantity for each item
    for item, quantity in storeManager.items():
        print(item, quantity)

### Date and Time

## Ex 1 - Calendar

import calendar

m, d, y = map(int, input().split())
i = calendar.weekday(y, m, d)
l = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(l[i])

## Ex 2 - Time delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timezone
# Complete the time_delta function below.
def time_delta(t1, t2):
    tmp = t1.split()
    t1_dt = datetime.strptime(' '.join(tmp[1:]), '%d %b %Y %H:%M:%S %z')
    t1_dt_utc = t1_dt.astimezone(tz = timezone.utc)
    tmp = t2.split()
    t2_dt = datetime.strptime(' '.join(tmp[1:]), '%d %b %Y %H:%M:%S %z')
    t2_dt_utc = t2_dt.astimezone(tz = timezone.utc)
    return str(abs((t1_dt_utc - t2_dt_utc).days * 24 * 3600 + (t1_dt_utc - t2_dt_utc).seconds))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

### Exceptions

## Ex 1 - Exceptions

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        try:
            a, b = map(int, input().split())

            print(a//b)
        except Exception  as e:
            print("Error Code:", e)

### Built-ins

## Ex 1 - Athlete

#!/bin/python3

import math
import os
import random
import re
import sys


def sort_players(n,m,arr,k):
   arr.sort(key = lambda x: x[k])

def print_arr(arr,m):
    for l in arr:
        s = ""
        for i in range(m):
            s += str(l[i]) + " "
        print(s)


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sort_players(n,m,arr,k)
    print_arr(arr,m)

## Ex 2 - Zipped

L = []
N, M = map(int, input().split())
for i in range(M):
    L.append(list(map(float, input().split())))
for i in zip(*L) :
    print(sum(i)/len(i))

## Ex 3 - ginorts

s = input()
lc = []
uc = []
od = []
ed = []
for i in range(len(s)):
    if s[i].isdigit():
        if int(s[i])% 2 == 0:
            ed.append(s[i])
        else:
            od.append(s[i])
    elif s[i].islower():
        lc.append(s[i])
    elif s[i].isupper():
        uc.append(s[i])
out = ""
lc.sort()
uc.sort()
od.sort()
ed.sort()
for item in lc:
    out += item
for item in uc:
    out += item
for item in od:
    out += item
for item in ed:
    out += item
print(out)

### Python Functionals

## Ex 1 - Map and Lambda

cube = lambda x: (x**3) # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    arr = []
    for i in range(0,n):
        if(i==0):
            arr.append(0)
        if(i==1 or i==2):
            arr.append(1)
        elif(i>2):
            arr.append(arr[i-1] + arr[i-2])
    return arr
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

### Regex and Parsing challenges

## Ex 1 - Floating Point number

import re
T = int(input())
for i in range(T) :
    N = input()
    print (bool(re.match('^[-+]?[0-9]*\.[0-9]+$' , N))) 
    # ? means zero or one * means zero or more +means one or more

## Ex 2 - Regex.split()

regex_pattern = r"\W"	# Do not delete 'r'.
import re
print("\n".join(re.split(regex_pattern, input())))

## Ex 3 - Group(), Groups() & Groupdict()

import re
m = re.findall(r"([A-Za-z0-9])\1+",input())  #\1 refers to first match group
if bool(m) :
    print(m[0])
else:
    print(-1)

## Ex 4 - Re.findall() & Re.finditer()
import re
r = r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})([^aeiouAEIOU])"
l = re.findall(r, input())
if(len(l)>0):
    [print(c[0]) for c in l]
else: print(-1)

## Ex 5 - Re.start() & Re.end()

import re

s = input()
k = input()
match_objects = re.finditer(r''+ k[0] + '(?='+ k[1:] +')',s)
lst = list(map(lambda x: x.start(),match_objects))
if lst == []:
    print((-1, -1))
else:
    for item in lst:
        print((item, item + len(k) -1))

## Ex 6 - Substitution

import re

n = int(input())
for _ in range(n):
    s = input()
    s = re.sub(r"(?<=\s)\|\|(?=\s)", "or" , s)
    s = re.sub(r"(?<=\s)&&(?=\s)", "and" , s)
    print(s)

## Ex 7 - Validating Roman Numbers

import re
regex_pattern = r"^(I(?=X))?(X(?=C))?(C(?=M))?M{0,3}(I(?=X))?(X(?=C))?(C(?=M))?((?<=C|X|I)M)?(I(?=X))?(X(?=C))?(C(?=D))?D?(I(?=X))?(X(?=C))?C{0,3}(I(?=X))?(X(?=L))?L?(I(?=X))?X{0,3}(I(?=V))?V?I{0,3}$"
print(str(bool(re.match(regex_pattern, input()))))


## Ex 8  - Validating phone numbers
import re

for _ in range(int(input())):
    m = re.match("^[789]\d{9}$", input())
    if bool(m) == True:
        print("YES")
    else:
        print("NO")

## Ex 9  - Validating and Parsing Email Addresses

import email.utils as email
import re

n = int(input())

for _ in range(n):
    m = email.parseaddr(input())
    regex = r"^[a-zA-Z][\w.-]+@[a-z]+\.[a-z]{1,3}$"
    res = re.search(regex, m[1])
    if res:
        print(email.formataddr((m[0], m[1])))

## Ex 10  - Hex Color Code

import re

r = r"#[0-9A-Fa-f]{3,6}\W"
n = int(input())
ls = []
for _ in range(n):
    line = input()
    if((len(line.split())<=1) or ('{' in line.split())):
       continue
    l = re.findall(r, line)
    [ls.append(s[:len(s)-1]) for s in l]
[print(s) for s in ls]

## Ex 11 - Html parser part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for (name, value) in attrs:
            print("->", name, ">", value)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for (name, value) in attrs:
            print("->", name, ">", value)


if __name__ == "__main__":

    parser = MyHTMLParser()
    n = int(input())

    for _ in range(n):
        line = input()
        parser.feed(line)

## Ex 12  - Html parser part 2


from html.parser import HTMLParser

class MySecondHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        if(len(data.split("\n"))>1):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if(data.strip()):
            print(">>> Data")
            print(data)
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MySecondHTMLParser()
parser.feed(html)
parser.close()

## Ex 13 - Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLDetector(HTMLParser):
    
        def handle_starttag(self, tag, attrs):
            print(tag)
            for (name, value) in attrs:
                print("->", name, ">", value)
html = ""

for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLDetector()
parser.feed(html)
parser.close()


## Ex 14  - Validating UID

import re

for _ in range(int(input())):
    s = input()
    v = True
    if re.match(r"^[a-zA-Z0-9]{10}$", s) == None: sur = False
    m = re.findall(r"([\w*]).*\1", s)
    if m != []: v = False
    m = re.findall(r"[A-Z]", s)
    if len(m) < 2: v = False
    m = re.findall(r"[0-9]", s)
    if len(m) < 3: v = False

    print("Valid") if v == True else print("Invalid")


## Ex 15  - Validating Credit Card Numbers

import re

for _ in range(int(input())):
    c = input()
    print ("Valid") if re.match(r"^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$", c) and re.findall(r"(\d)-?\1-?\1-?\1", c) == [] else print ("Invalid")
        

## Ex 16  - Validating Postal Codes

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

## Ex 17  - Matrix Script

#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

reading = input().rstrip().split()
n = int(reading[0])
m = int(reading[1])
mtx = []
for _ in range(n):
    read = input()
    mtx.append(read)
columns = zip(*mtx)
l = []
for col in columns:
    l += list(col)
s = ''.join(l)
print(re.sub(r"(?<=[a-zA-Z0-9])([!@#$%&]|\s)+(?=[a-zA-Z0-9])", " ", s))

### XML

## Ex 1 - Find the Score

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    start = 0
    start +=  len(node.attrib)
    for child in node:
        start += get_attr_number(child)
    return start


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
 
## Ex 2 - Find the Maximum Depth

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    for child in elem:
        depth(child, level)
    if level > maxdepth:
        maxdepth = level

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

### Closures and Decorations

## Ex 1 - Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


## Ex 2 - Name Directory

import operator

def person_lister(f):
    def inner(people):
        for i in range(len(people)):
            people[i][2] = int(people[i][2])
        people.sort(key=lambda x: x[2])
        for i in range(len(people)):
            people[i] = f(people[i])
        return(iter(people))
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


### Numpy

## Ex 1 - Arrays

import numpy

def arrays(arr):
    a = numpy.array(arr,float)
    return numpy.flip(a)
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

## Ex 2 - Shape and Reshape

arr = numpy.array(list(map(int, input().split())))
print(numpy.reshape(arr, (3, 3)))

## Ex 3 - Transpose and Flatten

import numpy

n, m = map(int, input().split())
my_list = []
for _ in range(n):
    my_list.append(list(map(int, input().split())))
arr = numpy.array(my_list)
print(numpy.transpose(arr))
print(arr.flatten())

## Ex 4 - Concatenate

import numpy


n, m, p = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
a = numpy.array(lst)
lst = []
for _ in range(m):
    lst.append(list(map(int, input().split())))
b = numpy.array(lst)
print(numpy.concatenate((a, b), axis = 0))


## Ex 5 - Zeros and Ones

import numpy

axis = tuple(map(int, input().split()))
print(numpy.zeros(axis, dtype = numpy.int))
print(numpy.ones(axis, dtype = numpy.int))

## Ex 6 - Eye and Identity

import numpy

n, m = map(int, input().split())
a = numpy.eye(n, m)
#forced to accept!
print(str(a).replace('1',' 1').replace('0',' 0'))

## Ex 7 - Array Mathematics

import numpy

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
a = numpy.array(lst)
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
b = numpy.array(lst)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)


## Ex 8 - Floor, Ceil and Rint

import numpy

# for hackerrank!
numpy.set_printoptions(sign=' ') 
a = numpy.array(list(map(float, input().split())))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

## Ex 9 - Sum and prod

import numpy

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
arr = numpy.array(lst)
print(numpy.prod(numpy.sum(arr, axis = 0)))

## Ex 10 - Min and Max

import numpy

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
arr = numpy.array(lst)
print(numpy.max(numpy.min(arr, axis = 1)))

## Ex 11 - Mean, var, std

import numpy

numpy.set_printoptions(legacy='1.13') #Same here
n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
arr = numpy.array(lst)
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(numpy.std(arr))

## Ex 12 - Dot and cross

import numpy

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
a = numpy.array(lst)
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
b = numpy.array(lst)
print(numpy.dot(a, b))

## Ex 13 - Inner and Oute

import numpy

a = numpy.array(list(map(int, input().split())))
b = numpy.array(list(map(int, input().split())))
print(numpy.inner(a, b))
print(numpy.outer(a, b))

## Ex 14 -Polynomials

import numpy

coe = list(map(float, input().split()))
print(numpy.polyval(coe, int(input())))


## Ex 15 - Linear Algebra

import numpy

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(float, input().split())))
arr = numpy.array(lst)
print(round(numpy.linalg.det(arr), 2))

# § Problem 2
# 

## Ex 1 - Birthday Cake

#!/bin/python3

import math
import os
import random
import re
import sys
def birthdayCakeCandles(ar):
    return ar.count(max(ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    fptr.write(str(result) + '\n')
    fptr.close()

## Ex 2 - Kangaroo

#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # I just applied the constraints
    return 'YES' if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


## Ex 3 - Viral  Adv

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    likes = 2
    total_likes = 2
    if n == 1:
        return total_likes
    else:
        for i in range(2,n+1):
            # each day we have:
            likes = likes * 3 // 2
            total_likes += likes
        return total_likes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


## Ex 4 - Recursive Digit Sum

# Complete the superDigit function below.
def superDigit(n, k):
    digits = map(int, list(n))
    return aux_superDigit(str(sum(digits) * k))

# aux function
def aux_superDigit(p):
    if len(p) == 1:
        return int(p)
    else:
        digits = map(int, list(p))
        return aux_superDigit(str(sum(digits)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

## Ex 5 - Insertion Sort 1


## Ex 6 - Insertion Sort 2

