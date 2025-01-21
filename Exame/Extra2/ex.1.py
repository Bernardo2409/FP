def validate(num):
    if type(num)==str and len(num)>=3:
        if num[0] == "+":
            return True if num[1:].isnumeric() else False
        else:
            return True if num.isnumeric() else False
            
    else:
        print("Número inválido!")
        return False
        #ta quase, ele so deixa é ainda ter + no meio, meter print nos falses


def register(clientes,oris,chamadas): #clientes={(ori):[(dest,dur),(dest,dur)],...}
    num=input("Telefone origem? ")
    while validate(num) == False:
        num=input("Telefone origem? ")
        validate(num)
    dest=input("Telefone destino? ")
    while validate(dest) == False:
        dest=input("Telefone destino? ")
        validate(dest)
    dur=int(input("Duração? (em segundos) "))
    chamada=(dest,dur)
    if num in clientes.keys():
        chamadas=clientes[num]
        chamadas.append(chamada)
        clientes[num]=chamadas
    else:
        chamadas=[]
        chamadas.append(chamada)
        clientes[num]=chamadas
    oris.add(num)
    return clientes, oris

def readfile(clientes,oris,chamadas):
    ficheiro=input("Ficheiro? ")
    with open(ficheiro) as file:
        for line in file:
            data=line.split()
            chamada=(data[1],data[2])
            if data[0] in clientes.keys():
                chamadas=clientes[data[0]]
                chamadas.append(chamada)
                clientes[data[0]]=chamadas
            else:
                chamadas=[]
                chamadas.append(chamada)
                clientes[data[0]]=chamadas
            oris.add(data[0])
    return oris, clientes


def listar(oris):
    oris=sorted(oris)
    print("Clientes: ", oris)

def fatura(clientes):
    total=0
    num=input("Número do cliente? (se quiser voltar para trás, prima b) ")
    if num in clientes.keys():
        print("Fatura do cliente ", num)
        print("{}{:>18}{:>23}".format("Destino", "Duração", "Custo"))
        for f in clientes[num]: #f é cada chamada do cliente
            if f[0][0] =="2":
                c=0.02
            elif f[0][0] =="+":
                c=0.80
            elif f[0][0]==f[0][1]: 
                c=0.04
            else:
                c=0.10
            custo=(int(f[1])/60)*c
            total+=custo
            print("{}{:>17}{:>22}".format(f[0], f[1], round(custo,2)))
        print("{:>23}{:>25}".format("Total:",round(total,2)))
    elif num=="b" or num =="B":
        main()
    else:
        fatura(clientes)
        
def main():
    print("Bem-vindo ao nosso programa de telecomunicações.")
    print("O que deseja fazer?")
    print("1) Registar chamada")
    print("2) Ler ficheiro")
    print("3) Listar clientes")
    print("4) Fatura")
    print("5) Terminar")
    clientes={}
    oris=set()
    chamadas=[]
    while True:
        op=(input("Opção? "))
        if op=="1":
            clientes, oris = register(clientes,oris, chamadas)
        if op=="2":
            oris, clientes = readfile(clientes, oris, chamadas)
        if op=="3":
            listar(oris)
        if op=="4":   
            fatura(clientes)
        if op=="5":
            print("Obrigado! Volte sempre")
            exit()
main()