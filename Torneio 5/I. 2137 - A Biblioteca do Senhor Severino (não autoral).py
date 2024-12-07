import sys

def ordenar_codigos():
    input = sys.stdin.read().strip().splitlines()
    index = 0

    while index < len(input):
        N = int(input[index].strip())
        index += 1
        
        codigos = []
        for _ in range(N):
            codigos.append(input[index].strip())
            index += 1
        
        codigos.sort()
        
        for codigo in codigos:
            print(codigo)

if __name__ == "__main__":
    ordenar_codigos()
