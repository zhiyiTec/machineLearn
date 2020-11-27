# d = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}
# print(d)
# print(d["中国"])
#
# print(type(d))


# d = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}
# print("中国 in d:{}".format("中国" in d))
# print("d.keys():{}".format(d.keys()))
# print("d.values:{}".format(d.values()))


# 1.定义一个空字典
d = {}
print("定义一个空字典:{}".format(d))
# 2.向d中新增两个元素
d["a"] = 1
d["b"] = 2
print("向d中新增两个元素:{}".format(d))
# 3.修改第二个元素
d["b"] = 3
print("修改第二个元素:{}".format(d))
# 4.判断字符c是否是d键
print("判断字符c是否是d键:{}".format("c" in d))
