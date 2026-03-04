

import threading
import time

start = time.time_ns()

'''
In worker function, when calling an external library that do the heavy computing work, 
if the library is written with native code (C / C++ / CUDA), it will not hold GIL,
GIL only block Python bytecode, Python thread can work and run in parallel in this case. 
Libraries that release the GIL:
    NumPy, SciPy, PyTorch, TensorFlow, OpenCV, scikit-learn (many ops), Pillow (some ops)

Libraries that do NOT release the GIL:
    Pure Python code
    Most Python loops
    Custom C extensions that didn’t opt out

How can a library release the GIL?

In C extensions:

Py_BEGIN_ALLOW_THREADS
// heavy computation
Py_END_ALLOW_THREADS

If the library didn’t do this → no parallelism.
'''

def worker(num):
    total = 0
    # heavy computing
    for i in range(100_000_000):
        total += i
    print(f"Thread {num}: Finishing")


threads = []
for i in range(3):
    # args is a tuple, (i,) is a tuple with one element
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Wait for all threads to finish

end = time.time_ns()
print("total: ", end - start)

# one thread: ~= 3.8s
# with 3 threads: total ~= 16s