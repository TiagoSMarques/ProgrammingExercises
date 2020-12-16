# Question 20
# Level 3

# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield

from time import sleep


def devBy7(b):
    for i in range(b+1):
        if i % 7 == 0:
            yield i
            # sleep(0.5)


for d in devBy7(77):
    print(d)


# f = [*range(10)]
# print(f)
