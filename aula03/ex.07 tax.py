def tax(r):
    if r <= 1000: 
       numero = 0.1 * r
    elif 1000<r<=2000:
       numero = 0.2*r -100
    else:
       numero = 0.3 * r - 300
    return numero
def main():
    valor = int(input("valor? "))
    resultado = tax(valor)
    print("O valor depois é ", resultado )
main()
    
