

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

if __name__ == '__main__':
    print('result=', job(1))
