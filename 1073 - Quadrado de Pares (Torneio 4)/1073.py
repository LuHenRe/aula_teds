while True:
    n = int(input())
    if 5 < n < 2000:
        break

for i in range (2, n+1):
    if i % 2 == 0:
        j = i ** 2
        print(f"{i}^2 = {j}")
