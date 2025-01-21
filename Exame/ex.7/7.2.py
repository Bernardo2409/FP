lista = []
with open("ex.7/primeiro.txt", 'r', encoding='utf-8') as f:
    for char in f.readlines():
        if char != '\n':
            lista.append(int(char))
        if len(lista) == 10:  # Para garantir que apenas 10 números são adicionados
            break

print(lista)
