soma = 0
contador = 0
while True:
    x = int(input())
    if x > 0:
        soma += x
        contador += 1
    else:
        print(f"{soma / contador:.2f}")
        break
