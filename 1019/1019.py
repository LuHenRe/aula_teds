duracao = int(input())

horas = duracao // 3600 #Divisão inteira para calcular o número de horas.
min = (duracao % 3600) // 60 
seg = duracao % 60 
print(f"{horas}:{min}:{seg}") #1:1:1
# print(f{horas}:{min:02d}:{seg:02d}") #1:01:01
