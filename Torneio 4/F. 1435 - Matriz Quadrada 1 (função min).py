while True:
    N = int(input())
    
    if N == 0:
        break
    
    for i in range(N):
        linha = []
        for j in range(N):
            valor = min(i, j, N - 1 - i, N - 1 - j) + 1
            linha.append(valor)
        print(" ".join(f"{x:3}" for x in linha))
    
    print()
