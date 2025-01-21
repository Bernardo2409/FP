primeira, segunda = input("palavras").split()
percentagem = 100
percentagem_por_letra = 100/len(primeira)
if len(primeira) == len(segunda):
    for letra in range(len(primeira)):
        if primeira[letra] != segunda[letra]:
            percentagem = percentagem - percentagem_por_letra
if percentagem < 90:
    print("não sao amigas")
else: print("sao amigas")