
import threading
import time

def job1():
    print('T1'+'This is a thread of %s' % threading.active_count())
    print('T1'+'This is a thread of %s' % threading.enumerate())
    print('T1'+'This is a thread of %s' % threading.current_thread())
    print('T1' + 'start')
    for i in range(10):
        time.sleep(0.1)
    print('T1'+'finish')

def job2():
    print('T2'+'This is a thread of %s' % threading.active_count())
    print('T2'+'This is a thread of %s' % threading.enumerate())
    print('T2'+'This is a thread of %s' % threading.current_thread())
    print('T2' + 'start')
    print('T2' + 'finish')

def main():
    thread_add1 = threading.Thread(target=job1, name='T1')
    thread_add2 = threading.Thread(target=job2, name='T2')
    thread_add1.start()
    thread_add2.start()
    thread_add1.join()
    thread_add2.join()

    print('all done \n')

if __name__ == '__main__':
    main()

