# Write a Python class to convert an integer to a roman numeral
from time import time
import random

my_randoms = random.sample(range(2_001), 2_000)
# print(my_randoms)

s = time()


class convertRoman:
    def __init__(self):
        self._numerals = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }

    def convert(self, value=None):
        if type(value) is not int:
            print("Please insert an integer")
        else:
            return self._convert(value)

    def _convert(self, value):
        alowedDeviation = (-1, 0, 1, 2, 3)
        romanNum = ""
        i = 0

        while value > 0:

            digit = value % 10

            if digit != 0:

                for multip in [1, 5, 10]:
                    dev = digit - multip
                    if dev in alowedDeviation and multip * dev != 3:
                        numeral = self._getRoman(i, dev, multip)
                        break

                romanNum = numeral + romanNum

            i += 1
            value = (value - digit) // 10

        return romanNum

    def _getRoman(self, iteration, deviation, target):

        coef = 10 ** (iteration)
        index = target * coef
        apendix = self._numerals[coef]

        if deviation != -1:
            return self._numerals[index] + apendix * deviation
        else:
            return apendix + self._numerals[index]


Roman = convertRoman()
# print(Roman.convert(394))
for _ in range(0, 600):
    [Roman.convert(elem) for elem in my_randoms]

e = time()

print("Method 1 -> Results in: ", e - s)


# ---------------------Solution-------------------

s = time()


class py_solution:
    def int_to_Roman(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


for _ in range(0, 600):
    [py_solution().int_to_Roman(elem) for elem in my_randoms]
e = time()


print("Method 2 -> Results in: ", e - s)

# print(py_solution().int_to_Roman(1))
# print(py_solution().int_to_Roman(4000))
