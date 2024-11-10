A, B, C = map(float, input().split())

pi = 3.14159
area_triang_retang = A * C / 2
area_circ = pi * C ** 2
area_trap = (A + B) * C / 2
area_quad = B ** 2
area_retang = A * B

print("TRIANGULO: {:.3f}".format(area_triang_retang))
print("CIRCULO: {:.3f}".format(area_circ))
print("TRAPEZIO: {:.3f}".format(area_trap))
print("QUADRADO: {:.3f}".format(area_quad))
print("RETANGULO: {:.3f}".format(area_retang))
