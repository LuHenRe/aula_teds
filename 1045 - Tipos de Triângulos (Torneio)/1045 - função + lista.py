def triangulo(x, y, z):
    if y > x:
        x, y = y, x
    if z > x:
        x, z = z, x
    if z > y:
        y, z = z, y

    resultados = []

    if x >= y + z:
        return "NAO FORMA TRIANGULO"

    if x ** 2 == y ** 2 + z ** 2:
        resultados.append("TRIANGULO RETANGULO")
    if x ** 2 > y ** 2 + z ** 2:
        resultados.append("TRIANGULO OBTUSANGULO")
    if x ** 2 < y ** 2 + z ** 2:
        resultados.append("TRIANGULO ACUTANGULO")

    if x == y == z:
        resultados.append("TRIANGULO EQUILATERO")
    if x == y or y == z or x == z:
        resultados.append("TRIANGULO ISOSCELES")
    
    return "\n".join(resultados)

a, b, c = map(float, input("Digite os lados do triângulo (separados por espaço): ").split())

print(triangulo(a, b, c))
