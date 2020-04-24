#多进程爬虫(不同于多线程)

import time


def job(t):
    print('Start job ', t)
    time.sleep(t)               # wait for "t" seconds
    print('Job ', t, ' takes ', t, ' s')


def main():
    [job(t) for t in range(1, 3)]


t1 = time.time()
main()
print("NO async total time : ", time.time() - t1)