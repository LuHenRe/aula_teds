cod_peca1 = int(input())
num_peca1 = int(input())
valor_peca1 = float(input())

cod_peca2 = int(input())
num_peca2 = int(input())
valor_peca2 = float(input())

montante = num_peca1 * valor_uni_peca1 + num_peca2 * valor_uni_peca2
print("VALOR A PAGAR: R$ {:.2f}".format(montante))
