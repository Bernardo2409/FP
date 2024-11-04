def max2(first, second):    
    if first > second: 
        numero = first
    else : 
        numero = second
    return numero
    
def main():
    first = int(input("numero 1: "))
    second = int(input("numero 2: "))

    maior = max2(first, second)

    print ("O número maior é", maior )

main()
