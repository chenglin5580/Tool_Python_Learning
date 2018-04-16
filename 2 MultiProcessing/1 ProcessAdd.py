

import multiprocessing as mp

def job(a, d, q):
    print('aaaa')
    res = a + d
    q.put(res)

#11

if __name__=='__main__':

    q = mp.Queue()
    p1 = mp.Process(target=job, args=(1, 2, q))
    p2 = mp.Process(target=job, args=(3, 4, q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('res1', res1, 'res2', res2)
