# Write the recursive version for the fibonacci sequence
# F0=0, F1=1
# Fn=F(n-1)+F(n-2)


def nthNumber(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nthNumber(n - 1) + nthNumber(n - 2)


print(nthNumber(10))


# Recurvive factorial
def fact(n):
    if n != 1:
        return n * fact(n - 1)
    else:
        return 1


print(fact(4))

