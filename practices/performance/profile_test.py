import time 

def make_num(n):
    return list(range(1,n+1))

def sum_num(nums):
    total = 0 
    for i in nums:
        total = total + i
     
    return total

def sum_without_list(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def main():
    n = int(input("nの値を入力してください"))
    start_total = time.perf_counter()

    start = time.perf_counter()
    nums = make_num(n)
    end = time.perf_counter()
    make_elapsed = end - start
    ##N個のリスト作成時間

    start = time.perf_counter()
    total = sum_num(nums)
    end = time.perf_counter()
    sum_elapsed = end - start
    ##1~Nまでを足し合わせた合計時間

    start = time.perf_counter()
    direct_total = sum_without_list(n)
    end = time.perf_counter()
    direct_elapsed = end - start
    ##リストなしで早くなるか検証
    end_total = time.perf_counter()
    total_elapsed = end_total - start_total
    ##全体の処理の時間

    print("n:", n)
    print("total:", total)
    print("make_numbers elapsed:", make_elapsed, "seconds")
    print("sum_numbers elapsed:", sum_elapsed, "seconds")
    print("direct_total:", direct_total)
    print("sum_without_list elapsed:", direct_elapsed, "seconds")
    print("total elapsed:", total_elapsed, "seconds")

main()