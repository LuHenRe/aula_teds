lista = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        sequencia = []
        for y in range(1, x + 1):
            sequencia.append(str(y))  # Adiciona cada número convertido em string
        lista.append(" ".join(sequencia))

print("\n".join(lista))
