def factorial(n):
    i=1
    fatorial = 1
    while i < (n+1):
        fatorial *=i
        i+=1
    return fatorial

def output(n):
    string=""
    i=n
    while i !=0:
        string += str(i)
        string += "x"
        i-=1
    palavra = string[:-1]

    return palavra


def main():
    n = int(input("digite um nmr"))
    fact= factorial(n)
    out = output(n)
    print("{}! = {} = {}".format(n, out, fact))
main()
    
