import math
a, b, c = map(float,input().split())

delta = (b ** 2) - (4 * a * c)
double = a * 2

if delta == 0:
    print(-b/double)
elif delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x = (-b + math.sqrt(delta)) / double
    y = (-b - math.sqrt(delta)) / double
    print(f"R1 = {x:.5f}\nR2 = {y:.5f}")
