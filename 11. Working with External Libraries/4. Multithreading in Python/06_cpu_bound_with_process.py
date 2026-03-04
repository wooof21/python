

from multiprocessing import Process
import time

def worker(num):
    total = 0
    for i in range(100_000_000):
        total += i

# guard with this if statement, ensure child node does not spawn new processes
if __name__ == "__main__":
    start = time.time()

    processes = []
    for i in range(3):
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Total time:", time.time() - start)

# one process: 3.8
# 3 processes: 3.8