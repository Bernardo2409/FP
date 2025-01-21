# Complete o programa!

# a)
def loadFile(file, lst):
    file=open(file,"r")
    file.readline()
    for line in file:
        reg = []
        line = line.strip("\n")
        reg.extend(line.split("\t"))
        lst.append(reg)

# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    nota1=float(reg[-3])
    nota2=float(reg[-2])
    nota3=float(reg[-1])
    
    notafinal = (nota1 + nota2 + nota3) / 3
    return notafinal

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print("{:<6} {:^50} {:>4}".format("Numero", "Nome", "Nota"))
    for reg in lst:
        print("{:<6} {:^50} {:.1f}".format(reg[0], reg[1], notaFinal(reg))) 

# e)
def main():
    lst = []
    # ler os ficheiros
    loadFile("d:/UA/1ano/FP/aula06/school1.csv", lst)
    loadFile("d:/UA/1ano/FP/aula06/school2.csv", lst)
    loadFile("d:/UA/1ano/FP/aula06/school3.csv", lst)
    
    # ordenar a lista
    lst.sort(key=lambda reg: int(reg[0]))
    
    # mostrar a pauta
    printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()