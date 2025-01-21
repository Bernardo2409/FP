def ispalindrome(texto):
    espaços = texto.replace(" ","").lower()
    if espaços == espaços[::-1]:
        return True
def main():
    s = input("Diz uma cena qualquer")
    if ispalindrome(s):
        print("É um palíndromo")
    else: print("Não é um palíndromo")
main()