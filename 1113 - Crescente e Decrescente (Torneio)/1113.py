lista = []
while True:
    x, y = map(int, input().split())
    if x == y:
        break
    elif x > y:
        lista.append("Decrescente")
    else:
        lista.append("Crescente")

print("\n".join(lista))
