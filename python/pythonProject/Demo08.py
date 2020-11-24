import random
import time

# random.seed(10)
# print(random.random())

#
# pi = 0.0
# N = 100
# for k in range(N):
#     pi += 1 / pow(16, k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1/(8 * k + 5) - 1 / (8 * k + 6))
# print("圆周率为：{}".format(pi))

DARTS = 1000 * 1000
hits = 0.0  # 表示命中的数量
start = time.perf_counter()
for i in range(1, DARTS + 1):
    x = random.random()
    y = random.random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits / DARTS)
print("圆周率的值为：{}".format(pi))
print("运行时间：{:.5f}".format(time.perf_counter() - start))
