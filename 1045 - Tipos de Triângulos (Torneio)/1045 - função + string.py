def triangulo(x, y, z):
    if y > x:
        x, y = y, x
    if z > x:
        x, z = z, x
    if z > y:
        y, z = z, y

    resultado = ""

    if x >= y + z:
        return "NAO FORMA TRIANGULO"

    if x ** 2 == y ** 2 + z ** 2:
        resultado += "TRIANGULO RETANGULO\n"
    if x ** 2 > y ** 2 + z ** 2:
        resultado += "TRIANGULO OBTUSANGULO\n"
    if x ** 2 < y ** 2 + z ** 2:
        resultado += "TRIANGULO ACUTANGULO\n"

    if x == y == z:
        resultado += "TRIANGULO EQUILATERO\n"
    elif x == y or y == z or x == z:
        resultado += "TRIANGULO ISOSCELES\n"

    return resultado.strip()

a, b, c = map(float, input().split())

print(triangulo(a, b, c))
