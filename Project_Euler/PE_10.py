total = 0
print("Starting calculations...")

for possiblePrime in range(2, 2000000):
    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
    if isPrime:
        # print(possiblePrime)
        total += possiblePrime

print(total)
