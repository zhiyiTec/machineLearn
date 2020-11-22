import time


# t = time.gmtime()
# tf = time.strftime("%Y-%m-%d %H:%M:%S", t)
# print(tf)


def wait():
    time.sleep(3)


st = time.perf_counter()
timeStr = '2018-01-26 12:55:20'
td = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
# print(time.strftime("%Y-%m-%d %H:%M:%S",td))

wait()
te = time.perf_counter()
rt = te - st
print(rt)
