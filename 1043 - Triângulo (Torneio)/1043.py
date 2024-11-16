def triangulo(x, y, z):
    if x + y <= z or x + z <= y or y + z <= x:
        return f"Area = {(x + y) / 2 * z:.1f}"
    else:
        return f"Perimetro = {x + y + z:.1f}"

a, b, c = map(float, input().split())

print(triangulo(a, b, c))
