import time
import random

def no_branch(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

def predictable_branch(numbers):
    total = 0
    for x in numbers:
        if x >= 0:
            total += x
    return total

def random_branch(numbers):
    total = 0
    for x in numbers:
        if x == 1:
            total += x
    return total

n = int(input("nの値を入力してください\n"))
print("n=100,000~10,000,000")

numbers = [1] * n
random_numbers = [random.randint(0, 1) for _ in range(n)]
#リスト内包表記にチャレンジ
# randint(0,1)で0　or　1のリストを作成（ともに５０％の割合）
# #

start = time.perf_counter()
result1 = no_branch(numbers)
end = time.perf_counter()
elapsed1 = end - start

start = time.perf_counter()
result2 = predictable_branch(numbers)
end = time.perf_counter()
elapsed2 = end - start

start = time.perf_counter()
result3 = random_branch(random_numbers)
end = time.perf_counter()
elapsed3 = end - start

print("no branch result:", result1)
print("no branch elapsed:", elapsed1, "seconds")

print("predictable branch result:", result2)
print("predictable branch elapsed:", elapsed2, "seconds")

print("random branch result:", result3)
print("random branch elapsed:", elapsed3, "seconds")