#1.0 Introduction

"""
Welcome to Introduction for Health Data Analytics. In this first training task we will get familiarized with Python. Please if you haven't done so already download Anaconda from: https://www.anaconda.com/products/individual. 
Anaconda comes with a bunch of data science packages already installed which will make things a lot easier for us.
First we we learn a little bit about coding in Python, although many of you will already have some experience with this, it won't hurt to refresh your memory!
Task 1:
List all the Data Types of Python with examples.
"""
#Text Type:  str
a = "string"
#Numeric Types:  int, float, complex
b = 1
c = 1.1
d = 1 + 1j
#Sequence Types:     list, tuple, range
e = ["apple", "banana"]
f = ("apple", "banana")
g = range(6)
#Mapping Type:   dict
cities_council = {
    "Elgin" : "Moray",
    "Inverness" : "Highlands",
    "Aberdeen" : "Aberdeen City"}
#Set Types:  set, frozenset
h = {"apple", "banana"}
freeze_f = frozenset(f)
#Boolean Type:   bool
bool_True = True
bool_False = False
#Binary Types:   bytes, bytearray, memoryview

"""
Task 2:
Other useful ways of storing data are in List, Arrays and Tuples. Create one of each and assign them to the variables a, b and c respectively.
"""
a = ["item1", "item2"]
import numpy as np
c = ([1,2,3,4], [5,6,7,8])
b = np.array(c) 
print(b)
print(c)
"""
Task 3:

We are also interested in becoming good software developers so we will need to use conditional, loops. 
Write an statement where the summation of a variable x+1 will be calculated if the value of x is greater than 2.
"""
x = 2.1
if x > 2:
    x = x + 1



#Now incorporate a for loop to calculate the value of n(x+1) for n repetitions where n=3. Store each value of the for loop in an array named y.
x = 1
n = 3
y = []
for i in range(1,n+1):
    x = i*(x + 1)
    y += [x]
print(x)
print(y)
"""
Task 4:

Finally we will have a look at creating functions. Functions allow us to compute processes much faster without having to repeat lines of code. Using your code from Task 3, create a function called 'my_cool_function', 
which takes in the value x and will compute the n(x+1) if x is greater than 2 and for n repetitions where values will be stored in an array named y. Your function will return y.
"""

def my_cool_func(x, n):
    y = []
    if x > 2:
        for i in range(1,n+1):
            x = i*(x + 1)
            y += [x]
    return y

print(my_cool_func(2.1,3))
# That is your first introductory python coding assignment completed! Hopefully you are now comfortable basic coding in Python!
