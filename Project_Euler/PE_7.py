count = 0

for possiblePrime in range(2, 1000000):
    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break

    if isPrime:
        count += 1
        if count == 10001:
            print(possiblePrime)
            break

