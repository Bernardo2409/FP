a,b,c = map(int,input().split())
lista = [a,b,c]
menor = lista[0]
for _ in range(3):
    for i in lista:
        if i < menor:
            menor = i
    lista.remove(menor)
    print(f"{menor}",end =' ')
    if len(lista)> 0:
        menor = lista[0]
   


