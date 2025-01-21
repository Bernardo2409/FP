lista = [1,2,3]
nova_lista = []
for i in range(len(lista)):
    nova_lista.append(sum(lista[:i+1]))
print(nova_lista)