def countdown(N):
    while N > 0:
        print(N)
        N = N -1

def main():
    N = int(input("Escreve um número inteiro"))
    countdown(N)
    
main()