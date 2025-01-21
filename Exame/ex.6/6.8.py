lista = [[1,2,3],[4,5,6],[7,8,9]]
nova_lista = []
descartavel = []
for i in range(len(lista)):
    descartavel = []
    for j in range(len(lista[i])):
        descartavel.append(lista[-j-1][i])
    nova_lista.append(descartavel)

print(nova_lista)
    


' 1 2 3'  '7 4 1'
'4 5 6'  '8 5 2'
'7 8 9'  '9 6 3'