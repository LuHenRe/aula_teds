while True:
    N = int(input())
    
    if N == 0:
        break

    maior_valor = 2 ** (2 * (N - 1))

    T = len(str(maior_valor))
    
    for i in range(N):
        linha = []
        for j in range(N):
            valor = 2 ** (i + j)
            linha.append(valor)
        
        print(" ".join(f"{x:>{T}}" for x in linha))
    
    print()
