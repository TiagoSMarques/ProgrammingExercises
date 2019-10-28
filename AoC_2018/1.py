# Here are other example situations:

# +1, +1, +1 results in  3
# +1, +1, -2 results in  0
# -1, -2, -3 results in -6
# Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

###--------------------Part1-----------------------###

from time import time


s = time()


def dataRead(file):

    with open(file, "r") as f:
        for line in f:
            value = int(line)
            yield value


result = 0
for value in dataRead("1.txt"):
    result += value


print("A: ", result)


###--------------------Part2-----------------------###


frequencies = {0}
freq = 0
dup = True

while dup:
    for value in dataRead("1.txt"):
        freq += value
        if freq not in frequencies:
            frequencies.add(freq)
        else:
            dup = False
            print("B: ", freq)
            break

e = time()
print("Calculated in: %.3f" % (e - s))


# import itertools

# with open('1.txt') as f:
# 	numbers = list(map(int, f.readlines()))

# 	print("A", sum(numbers))

# 	seen = set([0]) # set is about 16.000 times faster in this case
# 	for a in itertools.accumulate(itertools.cycle(numbers)):
# 		if a not in seen:
# 			seen.add(a)
# 		else:
# 			print("B", a)
# 			break
