lista = [0]
while True:
    n = int(input())
    if 0 < n < 46:
        break

contador = 1
soma = 0
anterior = 0
atual = 1

while contador < n:
    lista.append(atual)
    soma += atual
    anterior, atual = atual, anterior + atual
    contador += 1

print(" ".join(map(str, lista)))
