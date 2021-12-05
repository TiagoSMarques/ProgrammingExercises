from time import time

s = time()


def dataRead(file):
    with open(file, "r") as f:
        for line in f:
            yield line


pass_ok = 0

for line in dataRead("inp_2_a.txt"):  # iterate over the word

    vals, letter, pw = line.split(" ")
    v_min, v_max = map(int, vals.split("-"))
    inst = 0

    for char in pw:
        if char == letter[0]:
            inst = inst + 1
    if inst >= v_min and inst <= v_max:
        pass_ok = pass_ok + 1

print("problem 1: ", pass_ok)


# ------------------------Part_2------------------------------

ans_2 = 0

for line in dataRead("inp_2_a.txt"):  # iterate over the word

    vals, letter, pw = line.split(" ")
    pos1, pos2 = map(int, vals.split("-"))
    inst = 0

    if (pw[pos1 - 1] == letter[0]) != (pw[pos2 - 1] == letter[0]):
        ans_2 = ans_2 + 1


print("problem 2: ", ans_2)
e = time()
print("\nCalculated in: %.3fms" % ((e - s) * 1000))
