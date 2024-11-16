salario = float(input())

if 0 <= salario <= 400.00:
    print(f"Novo salario: {salario * 1.15:.2f}")
    print(f"Reajuste ganho: {salario * 1.15 - salario:.2f}")
    print(f"Em percentual: {((salario * 1.15 / salario) - 1.0) * 100:.0f} %")
elif 400.01 <= salario <= 800.00:
    print(f"Novo salario: {salario * 1.12:.2f}")
    print(f"Reajuste ganho: {salario * 1.12 - salario:.2f}")
    print(f"Em percentual: {((salario * 1.12 / salario) - 1.0) * 100:.0f} %")
elif 800.01 <= salario <= 1200.00:
    print(f"Novo salario: {salario * 1.1:.2f}")
    print(f"Reajuste ganho: {salario * 1.1 - salario:.2f}")
    print(f"Em percentual: {((salario * 1.1 / salario) - 1.0) * 100:.0f} %")
elif 1200.01 <= salario <= 2000.00:
    print(f"Novo salario: {salario * 1.07:.2f}")
    print(f"Reajuste ganho: {salario * 1.07 - salario:.2f}")
    print(f"Em percentual: {((salario * 1.07 / salario) - 1.0) * 100:.0f} %")
else:
    print(f"Novo salario: {salario * 1.04:.2f}")
    print(f"Reajuste ganho: {salario * 1.04 - salario:.2f}")
    print(f"Em percentual: {((salario * 1.04 / salario) - 1.0) * 100:.0f} %")
