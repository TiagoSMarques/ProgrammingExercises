# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


a = str(9)
# list = [a, 2*a, a+a+a, a+a+a+a]
pattern = [i*a for i in range(1, 5)]

print(sum(map(int, pattern)))
print(sum(int(i) for i in pattern))
