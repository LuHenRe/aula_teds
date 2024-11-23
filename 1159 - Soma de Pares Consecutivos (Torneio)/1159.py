lista = []

while True:
    x = int(input())
    if x == 0:
        break
    else:
        if x % 2 != 0:
            x += 1

        soma = 0
        for i in range(5):
            soma += x
            x += 2
        
        lista.append(soma)

print("\n".join(map(str, lista)))
