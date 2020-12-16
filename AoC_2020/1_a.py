# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579

# --------------------------------------Part_1------------------------------------------------
with open("inp_1_a.txt") as iV:
    arrayIn = []
    for line in iV:
        arrayIn.append(int(line))

sum = 0
pos = 0
ans = 0

for pos in range(len(arrayIn)):
    v1 = arrayIn[pos]
    for i in arrayIn[1:]:
        sum = v1 + i
        if sum == 2020:
            ans = v1 * i
            break
    else:
        continue
    break

# print(ans)

# --------------------------------------Part_2------------------------------------------------

sum = 0
pos = 0
ans = 0

for pos in range(len(arrayIn)):
    v1 = arrayIn[pos]
    for v2 in arrayIn[1:]:
        for v3 in arrayIn[2:]:
            sum = v1 + v2 + v3
            if sum == 2020:
                print(v1, v2, v3, sum)
                ans = v1 * v2 * v3
                break
        else:
            continue
        break
    else:
        continue
    break

print(ans)
