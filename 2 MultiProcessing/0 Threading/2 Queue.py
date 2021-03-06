

import threading
from queue import Queue


def job(iii, l, q):
    print('xiancheng', iii, 'start')
    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)
    print('xiancheng', iii, 'finish')


def main():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [3, 4, 5], [4, 4, 4], [5, 5, 5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(i, data[i], q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)





if __name__ == '__main__':
    main()