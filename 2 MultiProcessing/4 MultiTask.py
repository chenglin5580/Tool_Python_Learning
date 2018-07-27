# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import multiprocessing as mp
import time
from scipy.optimize import root


def job(i):
    print('Task ', i, 'beginning')
    res = root(problem, 0)
    time.sleep(1)
    print('Task ', i, 'end')
    return res.x

def problem(x):
    return 2*x-1


def multicore():
    pool = mp.Pool(processes=4)
    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])

if __name__ == '__main__':
    multicore()
