
res = []

for i in range(2000,3201):
    if (i%7==0) & (i%5!=0):
        res.append(i);

print(res)