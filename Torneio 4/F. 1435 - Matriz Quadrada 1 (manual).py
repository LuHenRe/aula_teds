while True:
    N = int(input())
    if N == 0:
        break
    
    for i in range(N):
        linha = []
        for j in range(N):
            distancia_superior = i
            distancia_inferior = N - 1 - i
            distancia_esquerda = j
            distancia_direita = N - 1 - j
            
            menor_distancia = distancia_superior
            if distancia_inferior < menor_distancia:
                menor_distancia = distancia_inferior
            if distancia_esquerda < menor_distancia:
                menor_distancia = distancia_esquerda
            if distancia_direita < menor_distancia:
                menor_distancia = distancia_direita

            valor = 1 + menor_distancia
            linha.append(valor)

        print(" ".join(f"{x:3}" for x in linha))
    
    print()
