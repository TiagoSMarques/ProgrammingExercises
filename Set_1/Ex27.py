# Question:
# Define a function that can convert a integer into a string and print it in console.

# Hints:

# Use str() to convert a number to string.


# def convertToint(string):
#     try:
#         return int(string)
#     except:
#         print("Please provide a number")
#         return None


# print(convertToint("33"))


def printValue(l):
    words = {}
    maxSize = 0

    for i in l:
        words[i] = len(i)
        maxSize = max(maxSize, words[i])

    [print(w) for w, pos in words.items() if pos == maxSize]


printValue(["one", "three", "sopas", "milho", "ovo"])
