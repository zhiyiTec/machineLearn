# 获取用户输入的数据
def getNum():
    nums = []
    isNumStr = input("请输入数字（回车退出）：")
    while isNumStr != "":
        nums.append(eval(isNumStr))
        isNumStr = input("请输入数字（回车退出）：")
    return nums


# 计算平均值
def mean(numbers):
    s = 0.
    for num in numbers:
        s += num
    return s / len(numbers)


# 计算用户输入的方差
def dev(numbers, mean):
    sdev = 0.
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1), 0.5)


# 计算中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        a1 = numbers[size // 2]
        a2 = numbers[size // 2 + 1]
        result = (a1 + a2) / 2
    else:
        result = numbers[size // 2]
    return result


def main():
    n = getNum()
    m = mean(n)
    print("平均值：{},方差:{:.2},中位数:{}".format(m, dev(n, m), median(n)))


main()
