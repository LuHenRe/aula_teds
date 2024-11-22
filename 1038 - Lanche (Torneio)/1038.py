def itens(codigo, qtdade):
    if codigo == 1:
        return qtdade * 4
    if codigo == 2:
        return qtdade * 4.5
    if codigo == 3:
        return qtdade * 5
    if codigo == 4:
        return qtdade * 2
    if codigo == 5:
        return qtdade * 1.5

cod, qtd = map(int, input().split())

print(f"Total: R$ {itens(cod, qtd):.2f}")
