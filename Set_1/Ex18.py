# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

import re
# import getpass
# Password = getpass()
from time import time
Username = "Tiago"
Passwords = ["ABd1234@1", "a F1#", "2w3E*",
             "2We3345", "assaswfsdfesdfefsdfe", "atua1#MaMA"]

s = time()


def isValid(password):
    chars = ["$", "#", "@"]
    valid = [0, 0, 0, 0]
    if len(password) < 6 or len(password) > 12:
        return False

    for char in set(password):
        if char.isupper():
            valid[0] = 1
        elif char.islower():
            valid[1] = 1
        elif char.isnumeric():
            valid[2] = 1
        elif char in chars:
            valid[3] = 1

    return sum(valid) == 4


Valid = [Password for Password in Passwords if isValid(Password)]
e = time()

print(Valid, "\nand took", e-s)

# Solutions:
# value = []
# items = ["ABd1234@1", "a F1#", "2w3E*", "2We3345", "assaswfsdfesdfefsdfe"]


# for p in items:
#     if len(p) < 6 or len(p) > 12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]", p):
#         continue
#     elif not re.search("[0-9]", p):
#         continue
#     elif not re.search("[A-Z]", p):
#         continue
#     elif not re.search("[$#@]", p):
#         continue
#     elif re.search("\s", p):
#         continue
#     else:
#         pass
#     value.append(p)

# e = time()

# print(value, "and took", e-s)
# print ",".join(value)
