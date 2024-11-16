a, b, c, d = map(int,input().split())

soma_cd = c + d
soma_ab = a + b

if b > c and d > a and soma_cd > soma_ab and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
