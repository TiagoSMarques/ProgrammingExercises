fib = [1, 2]
num = 0
total = 2
while num < 4000000 :
    num = fib[-2] + fib[-1]
    fib.append(num)
    if num % 2 == 0:
        total += num

print(total)
# 14930350
# 4613730
