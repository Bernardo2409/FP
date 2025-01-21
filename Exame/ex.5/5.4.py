teste1,teste2,teste3,teste4, exame = map(int,input("notas").split())

nota = 0.075 *(teste1 +teste2 +teste3+teste4) + 0.7*exame
if nota < 7:
    print("Reprovado")
elif 7 <= nota < 14:
    print("Oral")
else: print("Aprovado")