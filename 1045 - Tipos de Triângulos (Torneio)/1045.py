x, y, z = map(float, input().split())

if y > x:
    x, y = y, x
if z > x:
    x, z = z, x
if z > y:
    y, z = z, y

if x >= y + z:
    print("NAO FORMA TRIANGULO")
else:
    if x ** 2 == y ** 2 + z ** 2:
        print("TRIANGULO RETANGULO")
    if x ** 2 > y ** 2 + z ** 2:
        print("TRIANGULO OBTUSANGULO")
    if x ** 2 < y ** 2 + z ** 2:
        print("TRIANGULO ACUTANGULO")
    if x == y == z:
        print("TRIANGULO EQUILATERO")
    elif x == y or y == z or x == z:
        print("TRIANGULO ISOSCELES")
