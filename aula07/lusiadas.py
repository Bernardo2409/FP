import sys
dc = {}
with open("D:/UA/1ano/FP/aula07/examples/pg3333.txt", encoding="utf-8") as f:
    for line in f:
        for w in line.split():
            for letra in w:
                if letra.isalpha():
                    letra = letra.lower()
                    if letra in dc:
                        dc[letra] += 1
                    else: 
                        dc[letra] = 1
for letra, cont in dc.items():
    print(letra, cont)