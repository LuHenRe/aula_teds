valor = int(input())

cem = valor // 100
cinquenta = valor % 100 // 50
vinte = valor % 100 % 50 // 20
dez = valor % 100 % 50 % 20 // 10
cinco = valor % 100 % 50 % 20 % 10 // 5
dois = valor % 100 % 50 % 20 % 10 % 5 // 2
um = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1


print(valor)
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")
