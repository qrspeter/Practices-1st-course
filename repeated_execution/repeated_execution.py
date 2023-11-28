# calling function repeatedly by time.sleep

import time

interval = 1 # sec

def printing():
    print('Function called @', time.time() - start_time)
#    print('Program Executed @',time.asctime())

def just_sleep():
    while True:
        printing()
        time.sleep(interval)

def wait_sleep():
    starttime = time.time()
    while True:
        printing()
        time.sleep(interval - ((time.time() - starttime) % interval))

def monotonic_sleep():
    starttime = time.monotonic()
    while True:
        printing()
        time.sleep(interval - ((time.monotonic() - starttime) % interval))

import sched
def sched_calling():
    sc = sched.scheduler()
    while True:
        sc.enter(interval, 1, printing)
        sc.run()

import threading
def threading_calling():
    threading.Timer(interval, threading_calling).start()
    printing()

def threading_calling2():
    starttime = time.time()
    count = 0
    while True:
        time2sleep = -(time.time() - starttime) + (count + 1) *  interval
        t = threading.Timer(time2sleep, printing)
        t.start()
        t.join()
        count += 1


#If you want to do this without blocking your remaining code, you can use this to let it run in its own thread:
# https://stackoverflow.com/a/49801719
#
def threading_thread():
    threading.Thread(target=just_sleep()).start()

start_time = time.time()
# just_sleep() # ok
# monotonic_sleep() # ok 
# wait_sleep() # ok
# threading_thread() # ok
# threading_calling() # ok
threading_calling2() # ok
# sched_calling() # not ok


