n = int(input())

for _ in range(n):

    mensagem_codificada = input().strip()

    deslocamento = int(input())

    mensagem_decodificada = ""
    
    for letra in mensagem_codificada:
        novo_indice = (ord(letra) - deslocamento - ord('A')) % 26
        letra_original = chr(novo_indice + ord('A'))
        mensagem_decodificada += letra_original
    
    print(mensagem_decodificada)
