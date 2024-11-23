def itens(codigo, qtdade): 
    precos = [4, 4.5, 5, 2, 1.5]
    if 0 <= codigo < len(precos):
        return qtdade * precos[codigo]
    else:
        return 0

cod, qtd = map(int, input().split())

print(f"Total: R$ {itens(cod - 1, qtd):.2f}")
