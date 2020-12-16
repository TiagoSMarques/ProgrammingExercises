# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
from time import time

inString = "hello world! 123"
start = time()
# outDict = {}
outDict = {'Letters': 0, 'Digits': 0}
for i in inString:
    if i.isalpha():
        outDict['Letters'] += 1
    elif i.isdigit():
        outDict['Digits'] += 1

# outDict['Letters'] = len([i for i in inString if i.isalpha()])
# outDict['Digits'] = len([i for i in inString if i.isdigit()])
finish = time()

print(outDict)
print(finish-start)
