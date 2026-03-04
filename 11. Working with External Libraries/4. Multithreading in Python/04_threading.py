


import threading
import time

start = time.time_ns()

def worker(num):
    print(f"Thread {num}: Starting")
    '''
    sleep realse GIL, all threads not waiting for each other
    similar to I/O work, The interpreter:
        1. releases the GIL
        2. waits for the OS
        3. another thread acquires the GIL and runs
    '''
    time.sleep(3) # Simulate some work
    print(f"Thread {num}: Finishing")

threads = []
for i in range(3):
    # args is a tuple, (i,) is a tuple with one element
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Wait for all threads to finish
    
print("All threads completed.")

end = time.time_ns()
print("total: ", end - start)

'''
thread is good for:
    I/O-bound work:
        file reads/writes
        network calls
        database queries
        API requests

bad for:
    CPU-bound work:
        heavy math
        data processing
        ML inference loops
        tokenization in pure Python

Python threads share:
    the same memory
    the same process
    but are controlled by the GIL (Global Interpreter Lock)

The GIL:
    *** Only ONE thread executes Python bytecode at a time
    Even on multi-core CPUs
    Threads take turns, not true parallelism (for CPU work)

ThreadPoolExecutor (I/O):
    Create a pool of up to 10 threads, submit download_url(url) for every url in urls, 
    run them concurrently, and wait until all of them finish.

-------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=10) as pool:
    pool.map(download_url, urls)
-------------------------------------------------------------


with ... as pool:

This is a context manager:
    Automatically calls pool.shutdown(wait=True)
    Ensures all threads finish before exiting
    Prevents thread leaks


'''

'''
Python Multiprocessing (real parallelism):

    Spawns multiple OS processes
    Each process has:
        its own Python interpreter
        its own GIL
        its memory
    Can run on multiple CPU cores

e.g: higher memory usage

from multiprocessing import Process

def task(n):
    print(f"Task {n}")

processes = []
for i in range(5):
    p = Process(target=task, args=(i,))
    p.start()
    processes.append(p)

for p in processes:
    p.join()


ProcessPoolExecutor (CPU):

from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    pool.map(cpu_task, data)
'''