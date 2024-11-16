x = int(input())
y = int(input())
soma = 0

if y > x:
    x, y = y, x

for n in range (y, x+1):
    if n % 13 != 0:
        soma += n

print(soma)
