# For example, if you see the following box IDs:

# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.
# Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.
from time import time

s = time()


def dataRead(file):
    with open(file, "r") as f:
        for line in f:
            yield line


def checkSum():
    countDouble = 0
    countTriple = 0

    for line in dataRead("2.txt"):  # iterate over the word
        # whole word
        D = True
        T = True
        chars = [char for char in line]
        unique = set(chars)
        for char in unique:
            occur = chars.count(char)
            if occur == 2 and D:
                countDouble += 1
                D = False
            elif occur == 3 and T:
                countTriple += 1
                T = False

    print("A: ", countDouble * countTriple)


checkSum()


###--------------------------Part2------------------------------###


# def findID():
#     # build the dict
#     for line in dataRead("2.txt"):  # iterate over the word
#         candidates.update({line[:-1]: 0})

#     charPos = 0
#     # comparate chars
#     while True:
#         ww = list(candidates.keys())
#         elem = ww[charPos]
#         if charPos == 2:
#             break

#         for i in range(len(candidates)):
#             if ww[0][charPos] == ww[i][charPos]:
#                 candidates[ww[i]] = 1
#             else:
#                 pass
#         charPos += 1
#     print(candidates)


def findID():
    IDs = []
    candidates = []
    newCandidates = []

    # build the dict
    for line in dataRead("2.txt"):  # iterate over the word
        IDs.append(line[:-1])
    # print(IDs)

    # sizeID = len(IDs[0])
    # Cycle that removes a char from each word of the input list
    for pos in range(len(IDs[0])):

        # Build a list with the incomplete words
        candidates = [elem[:pos] + elem[(pos + 1) :] for elem in IDs]

        for index, item in enumerate(candidates):
            instances = candidates.count(item)
            # print(instances)
            if instances > 1:
                newCandidates.append(item)

    print(newCandidates[0])


findID()

e = time()
print("Calculated in: %.3fms" % ((e - s) * 1000))


# sorted_lines = sorted(lines)
# 	for i in range(len(sorted_lines)-1):
# 		str1 = sorted_lines[i]
# 		str2 = sorted_lines[i+1]
# 		is_equal = list(map(lambda x : x[0] == x[1], list(zip(str1, str2))))
# 		if Counter(is_equal)[False] == 1:
# 			print("B", "".join(str1[j] if is_equal[j] else "" for j in range(len(str1))))
# 			break
