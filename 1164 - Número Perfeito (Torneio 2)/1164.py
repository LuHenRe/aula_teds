lista = []
while True:
    n = int(input())
    if 1 <= n <= 20:
        break

for _ in range(n):
    x = int(input())
    soma = 0
    for y in range(1, x):
        if x % y == 0:
            soma += y
    if soma == x:
        lista.append(f"{x} eh perfeito")
    else:
        lista.append(f"{x} nao eh perfeito")
        
print("\n".join(map(str, lista)))
