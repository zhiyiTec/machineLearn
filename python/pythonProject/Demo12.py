
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# print("递归的结果为：{}".format(fact(3)))


# def rvs(s):
#     if s == "":
#         return s
#     else:
#         return rvs(s[1:]) + s[0]
#
#
# print("反转结果：{}".format(rvs("字符串反转")))


# def f(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return f(n - 1) + f(n - 2)
#
# print(f(10))


count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)


hanoi(3, "A", "C", "B")
print(count)
