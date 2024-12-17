fat = [1]
i = 1
while i <= 20:
  fat.append(i * fat[i - 1])
  i += 1

while True:
  try:
    x, y = map(int, input().split())
    print(fat[x] + fat[y])
  except EOFError:
    break
