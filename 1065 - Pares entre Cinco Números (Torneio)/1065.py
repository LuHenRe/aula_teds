a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

quant = 0
numeros = [a, b, c, d, e]
for numero in numeros:
    if numero % 2 == 0:
        quant += 1

print(f"{quant} valores pares")
