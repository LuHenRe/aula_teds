x = int(input())

while True:
    z = int(input())
    if z > x:
        break

soma = 0
contador = 0
atual = x

while soma <= z:
    soma += atual
    contador += 1
    atual += 1

print(contador)
