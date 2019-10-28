n = 1000

mults = set()

for i in range(n):
    if i % 3 == 0:
        mults.add(i)
    elif i % 5 == 0:
        mults.add(i)

print("sum: ", sum(mults))

