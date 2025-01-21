frutas = {'laranja': [10 , 1.50, 5 ,2.50],'banana':[20,2,20,3]}
lucro = 0
for fruta in frutas.values():
    lucro += fruta[2] * fruta[3] - fruta[1]*fruta[0]
print(lucro)

