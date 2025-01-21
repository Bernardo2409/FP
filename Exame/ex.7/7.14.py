inicioano, iniciomes, fimano, fimmes = map(int, input().split())
with open('ex.7/PIB1.txt','r',encoding='utf-8')as f:
    for line in f:
        column = [int(x) if x.isdigit() else x for x in line.strip().split()]
        if inicioano == column[0] and iniciomes == column[1]: 
            print(column[2])
            with open('ex.7/PIB2.txt','r',encoding='utf-8')as fileobj:
                for linha in fileobj:
                    coluna = [int(x) if x.isdigit() else x for x in linha.strip().split()]
                    if fimano == coluna[0] and fimmes == coluna[1]:
                        print(coluna[2])

