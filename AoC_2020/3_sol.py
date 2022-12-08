import math


def count_trees(forest, step):
    pos = (0, 0)
    nr_trees = 0

    while pos[1] < len(forest):
        if forest[pos[1]][pos[0] % len(forest[0])] == "#":
            nr_trees += 1

        pos = (pos[0] + step[0], pos[1] + step[1])

    return nr_trees


with open("inp_3_a.txt") as f:
    forest = []
    for row in f:
        forest.append(row.strip())

    print("Part 1: ", count_trees(forest, (3, 1)))
