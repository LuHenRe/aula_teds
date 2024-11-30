lista = []
n = int(input())
valores = {
    "1" : "2",
    "2" : "5",
    "3" : "5",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "3",
    "8" : "7",
    "9" : "6",
    "0" : "6"
}
for _ in range(n):
    soma = 0
    v = input()
    for digito in v:
        soma += int(valores[digito])
    lista.append(f"{soma} leds")

print("\n".join(map(str, lista)))
