
import threading


def job():
    print('This is a thread of %s' % threading.active_count())
    print('This is a thread of %s' % threading.enumerate())
    print('This is a thread of %s' % threading.current_thread())



if __name__ == '__main__':

    thread_add = threading.Thread(target=job)
    thread_add.start()

    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())