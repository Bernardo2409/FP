def sub_matriz(matriz, x,y,n,m):
    reciclagem = []
    submatriz = []
    for i in range(n):
        for j in range(m):
            reciclagem.append(matriz[x+i][y+j])
        submatriz.append(reciclagem)
        reciclagem = []

    return submatriz


print(sub_matriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]],1,1,2,2))


# 1 2 3 4
# 5 6 7 8
#9 10 11 12