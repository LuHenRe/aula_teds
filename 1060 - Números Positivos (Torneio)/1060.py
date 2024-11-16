a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

quant = 0
numeros = [a, b, c, d, e, f]
for numero in numeros:
    if numero > 0:
        quant += 1

print(f"{quant} valores positivos")
