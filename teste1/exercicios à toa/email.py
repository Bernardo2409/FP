def verificar_email(email):
    if "@" not in  email:
        return "E-mail inválida, falta o @"
    partes = email.split('@')
    print(partes)
    if len(partes) != 2:
        return "E-mail invalido mais que um @"
    
    print(partes[0])
    print(partes[1])
    if len(partes[0])<3:
        return "O e-mail tem de ter mais que 3 caracteres"
    if partes[1].count(".") >= 3:
        return "O e-mail tem mais que 2 pontos"
    
    return "E-mail inválido"

email = input("email????")

print(verificar_email(email))