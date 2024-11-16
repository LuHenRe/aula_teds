x = int(input())
y = int(input())

soma = 0
if y > x:
    y, x = x, y

for n in range (y+1, x):
    if n % 2 != 0:
        soma += n

print(soma)
