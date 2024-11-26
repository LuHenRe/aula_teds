lista = []
while True:
    v = int(input())
    if v <= 50:
        break

lista.append(f"N[{0}] = {v}")
x = 2 * v

for i in range (1, 10):
    lista.append(f"N[{i}] = {x}")
    x *= 2

print("\n".join(map(str, lista)))
