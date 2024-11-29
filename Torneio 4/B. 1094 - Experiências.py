n = int(input())
somaT = 0
somaC = 0
somaR = 0
somaS = 0

animais = {
    "C" : "coelhos",
    "R" : "ratos",
    "S" : "sapos"
}

for _ in range(n):
    q, t = map(str, input().split())
    q = int(q)

    if animais[t] == "coelhos":
        somaC += q
        somaT += q
        animal = animais[t]
    if animais[t] == "ratos":
        somaR += q
        somaT += q
        animal = animais[t]
    if animais[t] == "sapos":
        somaS += q
        somaT += q
        animal = animais[t]

percC = somaC / somaT * 100
percR = somaR / somaT * 100
percS = somaS / somaT * 100

print(f"Total: {somaT} cobaias")
print(f"Total de coelhos: {somaC}")
print(f"Total de ratos: {somaR}")
print(f"Total de sapos: {somaS}")
print(f"Percentual de coelhos: {percC:.2f} %")
print(f"Percentual de ratos: {percR:.2f} %")
print(f"Percentual de sapos: {percS:.2f} %")
