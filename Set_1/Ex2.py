import time
import sys

# sys.setrecursionlimit(1500)

start = time.time()

# def fat(num):
#     res=1;
#     if num == 0:
#         num =1
#     else:
#         while num > 0 :
#             res = res*num
#             num -=1
#     return res


def fat2(num):
    if num == 0:
        return 1
    else:
        return num*fat2(num-1)


# num = int (input("Insert an integer: "));
num = 8

# print(fat(num))
print(fat2(num))
# res =fat2(num)
end = time.time()
print(end-start)
