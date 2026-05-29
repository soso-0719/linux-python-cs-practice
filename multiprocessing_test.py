import time
import os
from multiprocessing import Pool

def sum_range(args):
    start, end = args
    total = 0

    for i in range(start, end):
        total += i

    return total
##CPU一つ
def single_process_sum(n):
    return sum_range((1, n + 1))

##CPU N個の処理
def multi_process_sum(n, workers):
    chunk_size = n // workers
    ##処理をプロセッサ分に分ける。
    ranges = []

    start = 1
    for worker_id in range(workers):
        if worker_id == workers - 1:
            end = n + 1
            ##割り切れない場合の処理
        else:
            end = start + chunk_size

        ranges.append((start, end))
        start = end
##今回における並行処理の核
    with Pool(processes=workers) as pool:
            part_results = pool.map(sum_range, ranges)
##pool.map()によって複数プロセスに配って実行している。
    
    return sum(part_results)

def decide_workers(requested_workers):
    cpu_count = os.cpu_count()

    if requested_workers < 4:
        return 4

    if requested_workers > cpu_count:
        return cpu_count

    return requested_workers

def main():
    n = int(input("nの値を入力してください\n"))
    requested_workers = int(input("使用するCPUの数を入力してください\n"))
    workers = decide_workers(requested_workers)
    start = time.perf_counter()
    single_total = single_process_sum(n)
    end = time.perf_counter()
    single_elapsed = end - start

    start = time.perf_counter()
    multi_total = multi_process_sum(n, workers)
    end = time.perf_counter()
    multi_elapsed = end - start

    print("cpu count:", os.cpu_count())
    print("workers:", workers)
    print("n:", n)
    print("single total:", single_total)
    print("single elapsed:", single_elapsed, "seconds")
    print("multi total:", multi_total)
    print("multi elapsed:", multi_elapsed, "seconds")

main()
