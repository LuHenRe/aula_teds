pokedex = set()
soma = 0
n = int(input())

for _ in range(n):
    pomekon = input()
    if pomekon not in pokedex:
        pokedex.add(pomekon)

print(f"Falta(m) {151 - len(pokedex)} pomekon(s).")
