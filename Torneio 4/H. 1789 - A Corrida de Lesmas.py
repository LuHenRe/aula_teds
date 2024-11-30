import sys

for line in sys.stdin:
    l = int(line.strip())
    
    if l == 0:
        break

    velocidades = list(map(int, input().split()))

    max_velocidade = max(velocidades)

    if max_velocidade < 10:
        print("1")
    elif max_velocidade >= 20:
        print("3")
    else:
        print("2")
