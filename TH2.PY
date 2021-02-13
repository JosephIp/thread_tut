import concurrent.futures
import time


def do(thread, seconds):
        if not seconds:
                raise NameError
        print(f'thread{thread}: sleeping {seconds} second(s)...')
        time.sleep(seconds)
        return f'thread{thread}: done sleeping...{seconds}                      '

start = time.perf_counter()

i = 0

#1
#with concurrent.futures.ThreadPoolExecutor() as executor:
#        f = executor.submit(do, i, 2.5)
#        print(f.result())

#2
#with concurrent.futures.ThreadPoolExecutor() as executor:
#        delay = [ 5, 4.5, 4, 3.5, 3, 2.5, 2 ]
#        r = [executor.submit(do, i, delay[i]) for i in range(len(delay))]
#
#        for f in concurrent.futures.as_completed(r): #this is a generator
#                print(f.result())                    #rtn in the order of completed task

#use map
with concurrent.futures.ThreadPoolExecutor() as executor:
        thd   = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
        delay = [ 5, 4.5, 4, 3.5, 3, 2.5, 0 ]
        rs = executor.map(do, thd, delay)

        for r in rs:
                print(r)                #rtn in the order of thread creation



stop = time.perf_counter()

print(f'all done in {round(stop-start, 2)} s')



