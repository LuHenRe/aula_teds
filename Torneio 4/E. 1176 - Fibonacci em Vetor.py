t = int(input())
lista = []

for _ in range(t):
    n = int(input())
    if 0 <= n <= 60:
        anterior, atual = 0, 1
        if n == 0:
            resultado = 0
        elif n == 1:
            resultado = 1
        else:
            for _ in range(2, n + 1):
                anterior, atual = atual, anterior + atual
            resultado = atual
        lista.append(f"Fib({n}) = {resultado}")

print("\n".join(lista))
