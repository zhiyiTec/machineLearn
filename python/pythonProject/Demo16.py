# ls = ["cat", "dog", "tiger", 1024]
# print("ls:{}".format(ls))
# lt = ls
# print("lt:{}".format(lt))
# lt.pop(0)
# print("删除lt0号位置之后的ls:{}".format(ls))
# print("删除lt0号位之后的lt{}".format(lt))


# ls = ["cat", "dog", "tiger", 1024]
# ls[1:2] = [1, 2, 3, 4, 5, 6]
# print("ls:{}".format(ls))
# del ls[::3]
# print("ls[::3]:{}".format(ls))
# ls *= 2
# print("ls *= 2:{}".format(ls))


# ls = ["cat", "dog", "tiger", 1024]
# ls.append(1234)
# print("ls.append(1234):{}".format(ls))
# ls.insert(3, "human")
# print('ls.insert:{}'.format(ls))
# ls.reverse()
# print("ls.reverse(){}".format(ls))


# 定义一个空列表
lt = []
# 向Lt中新增5个元素
lt += [1, 2, 3, 4, 5]
print("新增5个元素之后的结果为{}".format(lt))
# 修改lt中的第二个元素
lt[1] = 6
print("修改lt中的第二个元素:{}".format(lt))
# 向第二个位置增加一个元素
lt.insert(1, 7)
print("向第二个位置增加一个元素:{}".format(lt))
# 从lt中删除第一个元素
lt.pop(0)  # 或del lt[0]
print("从lt中删除第一个元素{}".format(lt))
# 删除lt中第0到第三个位置的元素，包含第三个位置
del lt[0:3]
print("删除lt中第0到第三个位置的元素，包含第三个位置:{}".format(lt))
# 判断lT中是否包含数字0
print("判断lT中是否包含数字0:{}".format(0 in lt))
# 向lt中新增数字0
lt.append(0)
print("向lt中新增数字0:{}".format(lt))
# 返回数字0在lt中的索引
print("返回数字0在lt中的索引:{}".format(lt.index(0)))
# lt的长度
print("lt的长度:{}".format(len(lt)))
# lt的最大元素
print("lt的最大元素:{}".format(max(lt)))
# lt的最小元素
print("lt的最小元素:{}".format(min(lt)))
# 清空lt
lt.clear()
print("清空lt:{}".format(lt))
