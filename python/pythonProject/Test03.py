# def dayUp(df):
#     dayup = 1
#     for i in range(365):
#         if i % 7 in [6, 0]:
#             dayup = dayup * (1 - 0.01)
#         else:
#             dayup = dayup * (1 + df)
#     return dayup
#
#
# dayFactor = 0.01
# while dayUp(dayFactor) < 37.8:
#     dayFactor += 0.001
# print("工作日的努力参数是：{:.3f}".format(dayFactor))


# import time
# scale = 50
# print("执行开始".center(scale // 2, "-"))
# start = time.perf_counter()
# for i in range(scale + 1):
#     a = "*" * i
#     b = "." * (scale - 1)
#     c = (i / scale) * 100
#     dur = time.perf_counter() - start
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
#     time.sleep(0.1)
# print("\n" + "执行结果".center(scale // 2, "-"))

# a = input()
# a = int(a)
# print("{0:-^20}".format(a ** 3))

# a = input()
# a = int(a)
#
#

#
#
# lineNum = getLine(a)
# j = 1
# # for i in range(lineNum):
# #     i+=1
# #     for k in range(j):
# #         print("*", end="")
# #     print()
# #     j = j + 2
# for i in range(lineNum):
#     print((' ' * ((a - j) // 2)) + ('*' * j) + (' ' * ((a - j) // 2)))

# def getLine(number):
#     i = 1
#     lineNum = 0
#     while i <= number:
#         i += 2
#         lineNum += 1
#     return lineNum
#
#
# num = eval(input())
# n = getLine(num)  # 计算行数
# m = 1
# for i in range(n):
#     print((' ' * ((num - m) // 2)) + ('*' * m) + (' ' * ((num - m) // 2)))
#     m += 2


def encryption(str, n):
    cipher = []
    for i in range(len(str)):
        if str[i].islower():
            if ord(str[i]) < 123 - n:  # ord('z')=122
                c = chr(ord(str[i]) + n)
                cipher.append(c)
            else:
                c = chr(ord(str[i]) + n - 26)
                cipher.append(c)
        elif str[i].isupper():
            if ord(str[i]) < 91 - n:  # ord('Z')=90
                c = chr(ord(str[i]) + n)
                cipher.append(c)
            else:
                c = chr(ord(str[i]) + n - 26)
                cipher.append(c)
        else:
            c = str[i]
            cipher.append(c)
    cipherstr = ('').join(cipher)
    return cipherstr


# 获得用户输入的明文
plaintext = input()
ciphertext = encryption(plaintext, 3)
print(ciphertext)
