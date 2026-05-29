import time
import numpy as np

def python_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def num_sum(n):
    numbers = np.arange(1, n + 1, dtype=np.int64)
    return np.sum(numbers)

def main():
    n = int(input("nの値を入力してください\n"))

    start = time.perf_counter()
    py_total = python_sum(n)
    end = time.perf_counter()
    py_elapsed = end - start

    start = time.perf_counter()
    np_total = num_sum(n)
    end = time.perf_counter()
    np_elapsed = end - start

    print("n:", n)
    print("python total:", py_total)
    print("python elapsed:", py_elapsed, "seconds")
    print("numpy total:", np_total)
    print("numpy elapsed:", np_elapsed, "seconds")

main()
