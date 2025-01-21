def shorten(texto):
    abreviacao = []
    for pal in texto.split():
        if pal and pal[0].isupper():
            abreviacao.append(pal[0])
                
    return ''.join(abreviacao)
            


def main():
    texto = str(input("Diz um nome de uma instituição"))
    print("A abreviação é", shorten(texto))

main()