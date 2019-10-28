
from time import sleep
from time import time

# ----------------------------------------------------------------------
# Don't hardcode parameters in decorator functions


def timer_d(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv
    return f


@timer_d  # decorator to wrap the funtion with the timer_d functionality
def add_dec(x, y=10):
    return x + y


@timer_d
def sub_dec(x, y=10):
    return x - y


print('add(10)', add_dec(10))
print('add(20, 30)', add_dec(20, 30))
print('add("a", "b")', add_dec("a", "b"))
print('sub(10)', sub_dec(10))
print('sub(20, 30)', sub_dec(20, 30))

# ----------------------------------------------------------------------

# This is a generator... don't eagerly compute. Return to user as they ask for it...


def compute():
    for i in range(10):
        sleep(.5)
        yield i

# for x in xs:
#    pass

# xi = iter(xs)    -> __iter__
# while True:
#   x = next(xi)   -> __next__


for val in compute():
    print(val)

# ----------------------------------------------------------------------

# Looping through a list an getting the addresses
List = ['a', 'b', 'c', 'd', 'e']


for index, item in enumerate(List, start=0):
    print(index, item)

# ----------------------------------------------------------------------
# Iterating over 2 lists

listL = ['a', 'b', 'c', 'd', 'e']
listC = ['A', 'B', 'C', 'D', 'E']

for small, large in zip(listL, listC):
    print(f'The Capital of {small} is {large}')

# ----------------------------------------------------------------------
# Acessing files, were you need to open and close them

with open('file.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(',')
word_count = len(words)
print(word_count)

# ----------------------------------------------------------------------
# Unpacking

a, b, c = (1, 2, 3)  # unpack in 3 vars
a, b, _ = (1, 2, 3)  # unpack in 2 vars (a and b) and forget the value 3


a, b, *c = (1, 2, 3, 4, 5)  # unpack and make a list c with remainig values

a, b, *_ = (1, 2, 3, 4, 5)  # unpack and discard remainig values

a, b, *c, d = (1, 2, 3, 4, 5, 6)  # unpack were d=6 and c=[3,4,5]

# ----------------------------------------------------------------------
# Dynamically create class attributes even using names from variables


class Person:
    pass


personInfo = {'first': 'Tiago', 'last': 'Marques'}
person = Person()

for key, value in personInfo.items():
    setattr(person, key, value)

# print(person.first)
# print(person.last)

# or

for key in personInfo.keys():
    print(getattr(person, key))
