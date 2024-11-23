lista = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        lista.append(" ".join(map(str, range(1, x + 1))))

print("\n".join(lista))
