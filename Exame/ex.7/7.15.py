with open('ex.7/clientes.txt','r',encoding='utf-8')as f:
    for line in f:
        line = line.strip('/n').split(' ')
        nome= line[0]
        sobrenome = line[1]
        nascimento = line[2].split('/')
        morada = line[3:-1]
        contacto = line[-1]
        if int(nascimento[2])< int(2000):
            nome=''.join(nome)
            morada = ' '.join(morada)
            ficheiro = f'ex.7/{nome} {sobrenome}.txt'
            with open(ficheiro,'w',encoding='utf-8')as fileobj:
                fileobj.write(f"Olá senhor {nome} {sobrenome}, que vive na {morada} \nEspero que esteja a ter uma boa tarde")
                




