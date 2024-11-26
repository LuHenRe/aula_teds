while True:
    v = int(input())
    if v <= 50:
        break

print(f"N[{0}] = {v}")
x = 2 * v

for i in range (1, 10):
    print(f"N[{i}] = {x}")
    x *= 2
