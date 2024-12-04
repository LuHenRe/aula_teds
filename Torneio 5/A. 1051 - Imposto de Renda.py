def imposto(salario):

    if 0.0 <= salario <= 2000.0:
        return "Isento"
    elif 2000.01 <= salario <= 3000.0:
        reais = (salario - 2000) * 0.08
        return f"R$ {reais:.2f}"
    elif 3000.01 <= salario <= 4500.0:
        reais = 1000 * 0.08 + (salario - 3000) * 0.18
        return f"R$ {reais:.2f}"
    else:
        reais = 1000 * 0.08 + 1500 * 0.18 + (salario - 4500) * 0.28
        return f"R$ {reais:.2f}"

dinheiro = float(input())
print(imposto(dinheiro))
