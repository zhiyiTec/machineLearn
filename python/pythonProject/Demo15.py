# A = {"python", 123, ("python", 123)}
# print(A)
# B = set("pypy123123")
# print(B)
# C = {"python", 123, "python", 123}
# print(C)

# A = {"p", "y", 123}
# B = set("pypym123")
# print("A-B:{}".format(A - B))
# print("B-A:{}".format(B - A))
# print("A&B:{}".format(A & B))
# print("A | B:{}".format(A | B))
# print("A ^ B", format(A ^ B))


# A={"p","y",123}
# for item in A:
#     print(item,end="")


# A = {"p", "y", 123}
# try:
#     while True:
#         print(A.pop(), end="")
# except:
#     pass

# A = {"p", "y", 123}
# print("p" in A)

# # 列表
# ls = ["p", "p", "y", "y", 123]
# s = set(ls)
# print(s)
# ls = list(s)  # 将集合转为列表
# print(ls)

creature = "cat", "dog", "tiger", "human"
print(creature[::-1])
color = (111, "blue", creature)
print(color[-1][2])
