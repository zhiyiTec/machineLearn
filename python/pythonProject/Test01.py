# TempStr = input("请输入带符号的温度值:")
# if TempStr[-1] in ['F', 'f']:
#     C = (eval(TempStr[0:-1]) - 32) / 1.8
#     print("转换后的温度为：{:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = 1.8 * eval(TempStr[0:-1]) + 32
#     print("转换后的温度为：{:.2f}F".format(F))
# else:
#     print("输入格式错误")

# print("Hello World")


#
# num = input()
# NUM = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
# for i in num:
#     i = int(i)
#     print(NUM[i], end="")


# TempStr = input()
# if TempStr[0] in ['F', 'f']:
#     C = (eval(TempStr[1:]) - 32) / 1.8
#     print("C{:.2f}".format(C))
# elif TempStr[0] in ['C', 'c']:
#     F = 1.8 * eval(TempStr[1:]) + 32
#     print("F{:.2f}".format(F))


Money = input()
if Money[0:3] == 'RMB':
    C = eval(Money[3:]) / 6.78
    print("USD{:.2f}".format(C))
elif Money[0:3] == 'USD':
    C = eval(Money[3:]) * 6.78
    print("RMB{:.2f}".format(C))
