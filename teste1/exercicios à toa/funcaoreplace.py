def trocar(palavra):
    if len(palavra) % 2 == 0:
        metade = len(palavra) //2
        
        palavra = palavra[0: metade-1] + palavra[metade] + palavra[metade-1] + palavra[metade+1:len(palavra)]

        print(palavra)
    else:
        print(palavra)
def change(palavra):
    metade = len(palavra) //2
    string = ""
    first = palavra[metade-1]
    second = palavra[metade]

    for n in range(metade-1):
        string += (palavra[n])
        
    string +=(second)
    string +=(first)

    for n in range(metade+1, len(palavra)):
        string += (palavra[n])
    print(string)

def main():
    str = input("diz uma palavra")
    trocar(str)
    change(str)

main()
        