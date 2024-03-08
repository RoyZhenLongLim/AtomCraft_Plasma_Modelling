import numba
import time

@numba.jit
def print_numbers():
    l = []
    for i in range(100000):
        l.append(i ** 2)

def time_function(func):
    start = time.time()
    func()
    end = time.time()
    print(f"Execution time: {(end - start) * 1e6:.0f} microseconds")

time_function(print_numbers)