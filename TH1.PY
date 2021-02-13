# VS CODE OPEN CMD PARLETTE
# CTRL+SHIFT+P

# CTRL + ` --> TOGGLE TERMINAL

# SHIFT+ALT+F -> FORMAT DOC

# enable powershell
# Set-ExecutionPolicy -ExecutionPolicy Unrestricted
# chk Get-ExecutionPolicy


import threading
import time

import sys

print(sys.version)
print(sys.executable)


def do(thread, seconds):
    print(f"thread{thread}: sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print(f"thread{thread}: done sleeping")


start = time.perf_counter()

pool = []
for i in range(10):
    t = threading.Thread(target=do, args=[i, 1.5])
    t.start()
    pool.append(t)

for t in pool:
    t.join()

stop = time.perf_counter()

print(f"all done in {round(stop-start, 2)} s")
