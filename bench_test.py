import time

def sumloop(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total

n = int(input("nの値を入力してください\n"))
print("n=10,000~10,000,000")

start = time.perf_counter()
result = sumloop(n)
end = time.perf_counter()
elapsed = end - start

print("n:", n)
print("result(１からｎまでの合計の値):", result)
print("elapsed:", elapsed, "seconds")