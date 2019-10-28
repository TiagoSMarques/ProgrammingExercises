import numpy

primes = []
for possiblePrime in range(2, 10000):
    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(possiblePrime)

p_fact = []
res = 1
it = 1

Or = 600851475143
n = Or

while numpy.prod(p_fact) != Or:
    fact = primes[it]
    if n % fact == 0:
        p_fact.append(fact)
        n = n / fact
        it = 1
    else:
        it += 1

print(max(p_fact))

# def primes(n):
#     primes = set()
#     for i in range(1, int(sqrt(n + 1))):
#         if n % i != 0:
#             primes.add(i)
#     return primes

# print(primes)
# print(primes(13195))
