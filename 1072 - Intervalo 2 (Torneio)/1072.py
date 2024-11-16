n = int(input())
qtd_in = 0
qtd_out = 0

for _ in range (0, n):
    x = int(input())
    if 10 <= x <= 20:
        qtd_in += 1
    else:
        qtd_out += 1

print(f"{qtd_in} in\n{qtd_out} out")
