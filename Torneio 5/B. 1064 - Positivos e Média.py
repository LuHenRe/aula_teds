val_pos = 0
soma = 0
for _ in range(6):
    a = float(input())
    if a > 0:
        val_pos += 1
        soma += a
media = soma / val_pos

print(f"{val_pos} valores positivos\n{media:.1f}")
