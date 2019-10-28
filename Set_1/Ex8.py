
inStringList = [x for x in input("Enter words: ").split(',')]

outStringList = inStringList[:]
outStringList.sort()

print(inStringList)
print(outStringList)
