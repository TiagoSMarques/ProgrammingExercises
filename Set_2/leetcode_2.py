from time import time

a = time()


class Solution:
    def fact(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * fact(n - 1)

    def Combinations(self, n, r):
        return sum(fact(n) / (fact(r) * fact(n - r)))

    def sumSubseqWidths(self, A: [int]) -> int:
        self.In = A
        size_A = len(A)
        width = 0
        r = 2
        size_Iter_Array = 2

        while r != size_A:
            ref_index = 0
            while ref_index != size_A:
                i = 0
                while i != size_A - (ref_index):
                    subsect = self.In[ref_index : ref_index + size_Iter_Array]
                    # print(ref_index, ref_index + size_Iter_Array, subsect)
                    # print(self.In[ref_index], self.In[ref_index + i])
                    # width += abs(self.In[ref_index] - self.In[ref_index + i])
                    i += 1

                ref_index += 1
            size_Iter_Array += 1
            print(size_Iter_Array)
        # print(width)
        return width


S = Solution()
# L = [2, 1, 3, 5]
S.sumSubseqWidths([2, 4, 1])

b = time()

print("results in: ", b - a)

import functools

a = [1, 2, 3]
print(a[0:2])


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


n = len(a)
Comb = sum(map(lambda r: fact(n) / (fact(r) * fact(n - r)), range(1, n + 1)))
print(Comb)

