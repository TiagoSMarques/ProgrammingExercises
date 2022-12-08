# even division by first 20 numbers

# start = 20

number = 20
answer = 0
aa = []
while True:
    aa = [div for div in range(3, 20) if number % div == 0]
    # print(number)
    if len(aa) == 17:
        answer = number
        break
    else:
        number += 2

print(answer)
