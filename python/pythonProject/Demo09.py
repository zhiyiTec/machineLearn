# def fact(n, *b):
#     s = 1
#     for i in range(1, n + 1):
#         s *= i
#     for item in b:
#         s *= item
#     return s
#
#
# result = fact(10, 1, 2, 3)
# print(result)

# def fact(n, m):
#     s = 1
#     for i in range(1, n + 1):
#         s *= i
#     return s // m, n, m
#
#
# print(fact(5, 2))
# a, b, c = fact(5, 2)
# print("a:{},b:{},c:{}".format(a, b, c))


n,s=10,100
def fact(n):
    global s
    for i in range(1,n+1):
        s*=i
    return s
