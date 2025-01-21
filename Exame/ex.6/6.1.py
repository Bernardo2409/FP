lista_idades = [17,18,19,17,20,21,24]
quantidade = len(lista_idades)
for i in lista_idades:
    print(i,end=' ')
print(lista_idades[::-1])
print(lista_idades[1:-1])
print(min(lista_idades),max(lista_idades))
print(sum(lista_idades))
print(len([x for x in lista_idades if x<19]))
print(17 in lista_idades)