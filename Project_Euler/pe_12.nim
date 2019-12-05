let i = 1
let num = 0

while true:
    let numfacts = 2
    num += i
    i += 1

    for fact in range(2, int(num / 2 + 1)):
        if num % fact == 0:
            numfacts += 1

    if numfacts >= 5:
        break


print("Valor", num)

# print(triangleFactor(7))
