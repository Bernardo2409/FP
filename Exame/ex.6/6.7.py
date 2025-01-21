lista = [[0,1,0],[1,1,1],[0,1,0]]
nova_lista = []
descartavel = []


for i in lista:
    descartavel = []
    for j in i:
        if j == 0:
            descartavel.append(1)
        else:
            descartavel.append(0)
    nova_lista.append(descartavel)
print(nova_lista)

