def matriz(largura, altura):
    matriz = []
    
    for _ in range(altura):
        matriz.append(tuple([1]*largura))
    return matriz





print(matriz(3,3))

#   1 1
#   1 1