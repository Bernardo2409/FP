def isPrime(n):
    d=1
    sum = 0
    if n ==1: return False
    while d<= n/2:
        if n % d ==0:
            sum +=1
        d +=1
    if sum == 1: return True
    else: return False
    
def main():
    n = int(input("insere um numero para verificar se é primo"))
    print("O número é primo?", isPrime(n))
    l= int(input("Até que número queres ver os números primos existentes?"))
    l=l+1
    for i in range(1,l):
        if isPrime(i) == True:
            print(i)
    print()
    print()
    lst= []
    for i in range(1,l):
        if isPrime(i) == True:
            lst.append(i)
    l=l-1           
    print("Os números primos até",l, "são:", lst)

main()