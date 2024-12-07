import sys

def calcular_ciclos(rastro, processos):
    ciclos = 0
    i = 0
    n = len(rastro)
    
    while i < n:
        if rastro[i] == 'R':
            leitura_count = 0
            while i < n and rastro[i] == 'R' and leitura_count < processos:
                leitura_count += 1
                i += 1
            ciclos += 1
        elif rastro[i] == 'W':
            ciclos += 1
            i += 1
    
    return ciclos

def main():
    input_data = sys.stdin.read().strip().split('\n')
    results = []
    
    for i in range(0, len(input_data), 2):
        rastro = input_data[i]
        processos = int(input_data[i + 1])
        resultado = calcular_ciclos(rastro, processos)
        results.append(resultado)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
