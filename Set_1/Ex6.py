# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
import math

def formula(D):
    C,H=50, 30
    return round(math.sqrt(2*C*D/H))

num=input("Enter Sring: ")
l=num.split(',')
res=[];

for i in l:
    i=int(i)
    res.append(formula(i))

print(res)