# calling function repeatedly by time.sleep

import time
interval = 1 # sec
 
class Interval_doing:
    start_time = 0
    counter = 1
    def __init__(self):
        self.start_time = time.time()
        
    def printing(self):
        print(f'Function called {self.counter} times @{time.time() - self.start_time}')
        time.sleep(0.5)
        self.counter += 1
    #    print('Program Executed @',time.asctime())

def just_sleep():
    while True:
        doing()
        time.sleep(interval)

def wait_sleep():
    starttime = time.time()
    while True:
        doing()
        time.sleep(interval - ((time.time() - starttime) % interval))

def monotonic_sleep():
    starttime = time.monotonic()
    while True:
        doing()
        time.sleep(interval - ((time.monotonic() - starttime) % interval))

import sched
def sched_calling():
    starttime = time.time()
    count = 0
 
    sc = sched.scheduler()
    while True:
        time2sleep = -(time.time() - starttime) + (count + 1) *  interval
        print(time2sleep)
        sc.enter(time2sleep, 1, doing) #printing_sc, (sc,))
        sc.run()
        count += 1

import threading
def threading_calling():
    threading.Timer(interval, lambda: threading_calling()).start()
    doing()
    print(1)

def threading_calling2():
    starttime = time.time()
    count = 0
    while True:
        time2sleep = -(time.time() - starttime) + (count + 1) *  interval
        t = threading.Timer(time2sleep, doing)
        t.start()
        t.join() # will wait until the thread `t` has finished
        # https://copyprogramming.com/howto/python-python-is-thread-timer-running
        count += 1
        print(f"{time2sleep=}")


#If you want to do this without blocking your remaining code, you can use this to let it run in its own thread:
# https://stackoverflow.com/a/49801719
#
def threading_thread():
    threading.Thread(target=just_sleep()).start()

def doing():
    my_doing.printing()
    # call method printing

if __name__ == "__main__":
    # create class object
    my_doing = Interval_doing() 


    # just_sleep() # ok
    # monotonic_sleep() # ok 
    # wait_sleep() # ok
#    threading_thread() # ok but slowly drift like a time.sleep(), no errors
#    threading_calling() # ok but small drift
#    threading_calling2() # ok no drift with time-starttime
    sched_calling() # ok no drift with time-starttime

# the only question is: do the thread/sched methods freeze the main func or not?

