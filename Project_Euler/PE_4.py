# palindrome


def getPalindrome():

    answer = 0
    for a in range(999, 100, -1):
        for b in range(999, 100, -1):
            number = str(a * b)
            # print(number)
            if number == number[::-1]:
                if int(number) > int(answer):
                    answer = number
    return answer


# number = "123"
# print(number[::-1])
# print(list(range(9, 1)))
# 90909
print(getPalindrome())
