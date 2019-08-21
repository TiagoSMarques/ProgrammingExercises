# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

inString = "Hello world!"
# outDict = {}
outDict = {'lCase': 0, 'uCase': 0}

for letter in inString:
    if letter.islower():
        outDict['lCase'] += 1
    elif letter.isupper():
        outDict['uCase'] += 1

print(outDict)
