from time import time

s = time()


def dataRead(file):
    with open(file, "r") as f:
        for line in f:
            yield line


def convert(strIn):
    l = []
    l[:0] = strIn
    return l


Mat = []

for line in dataRead("inp_3_a.txt"):  # iterate over the word
    row = []
    row = convert(line)
    if row[-1] == "\n":
        row.pop()
    Mat.append(row)

num_col = len(Mat[0])

dir_x = 0

ans = 0

for dir_y in range(len(Mat) - 1):
    # print(Mat[dir_y][dir_x])
    dir_x = (dir_x + 3) % num_col
    if dir_x == 0:
        dir_x = -1

    if Mat[dir_y + 1][dir_x] == "#":
        ans += 1

    # dir_y = dir_y + 1
    print("dir_x", dir_x)
    print("dir_y", dir_y + 1)

print(ans)
