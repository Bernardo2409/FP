def divisores(n):
    d=1
    lst=[]
    while n > d:
        if n % d == 0:
            lst.append(d)
        d+=1
    return lst

def classificar(a):
    
    lista = divisores(a)
    soma =sum(lista)
    if soma < a:
        print(a, "é um número deficiente")
    elif soma == a:
        print(a, "é um número perfeito")
    else: print(a, "é um número abundante")



    return soma

def main():
    n = int(input("Digite um número inteiro"))
    print(divisores(n))
    print(classificar(n))

main()