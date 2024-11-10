A, B, C = map(int, input().split())

M = (A + B + abs(A-B))/2
maior1 = (C + M + abs(C-M))/2
maior1 = int(maior1)

print(f"{maior1} eh o maior")
