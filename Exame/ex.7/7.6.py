def copia(ficheiro, nome):
    with open(ficheiro, 'r', encoding='utf-8') as f:
            with open(nome, 'w', encoding='utf-8') as fileobj:
                for line in f:
                    fileobj.write(line)


copia('ex.7\primeiro.txt', 'rei.txt')