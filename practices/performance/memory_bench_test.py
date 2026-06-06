import time

def sequential_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

n = int(input("nの値を入力してください\n"))
print("n=10,000~10,000,000")

numbers = list(range(1,n+1))

start = time.perf_counter()
result = sequential_sum(numbers)
end = time.perf_counter()

elapsed = end - start

print("n:", n)
print("result(１からｎまでの合計の値):", result)
print("elapsed:", elapsed, "seconds")
