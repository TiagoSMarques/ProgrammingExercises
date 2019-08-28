# Write a Python class to convert an integer to a roman numeral


class convertRoman:
    def convert(self, value=None):
        if type(value) is not int:
            print("Please insert an integer")
        else:
            return self._convert(value)

    def _convert(self, value):
        parsedValue = list(str(value))[::-1]
        alowedDeviation = [-1, 0, 1, 2, 3]
        # print(parsedValue)
        romanNum = []
        for i, n in enumerate(parsedValue):
            if n == 0:
                numeral = _getRoman(i, 0, n)
            else:
                devFrom1, devFrom5, devFrom10 = [int(n) - v for v in [1, 5, 10]]

                if devFrom1 in alowedDeviation and devFrom1 != 3:
                    numeral = self._getRoman(i, devFrom1, 1)
                elif devFrom5 in alowedDeviation:
                    numeral = self._getRoman(i, devFrom5, 5)
                else:
                    numeral = self._getRoman(i, devFrom10, 10)
            romanNum.insert(0, numeral)

        return "".join(romanNum)

    def _getRoman(self, iteration, deviation, target):
        numerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        num = 10 ** (iteration)
        index = target * num
        # print(index)
        apendix = numerals[num]

        if deviation == 0 and target != 0:
            return numerals[index]
        elif deviation == -1 and target != 1:
            return str(apendix + numerals[index])
        elif deviation == 1:
            return str(numerals[index] + apendix)
        elif deviation == 2:
            # apendix = numerals[index / 5]
            return str(numerals[index] + apendix + apendix)
        elif deviation == 3:
            # apendix = numerals[index / 5]
            return str(numerals[index] + apendix + apendix + apendix)
        else:
            return ""


Roman = convertRoman()

print(Roman.convert(894))


# ---------------------Solution-------------------
# class py_solution:
#     def int_to_Roman(self, num):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ''
#         i = 0
#         while  num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i += 1
#         return roman_num


# print(py_solution().int_to_Roman(1))
# print(py_solution().int_to_Roman(4000))
