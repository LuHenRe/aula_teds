valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
valorC = int(round(valor * 100))
print("NOTAS:")

for nota in notas:
    notaC = int(nota * 100)
    quantidade = valorC // notaC
    valorC %= notaC
    print(f"{quantidade:.0f} nota(s) de R$ {nota}.00")

print("MOEDAS:")

for moeda in moedas:
    moedaC = int(moeda * 100)
    quantidade = valorC // moedaC
    valorC %= moedaC
    print(f"{quantidade:.0f} moeda(s) de R$ {moeda:.2f}")
