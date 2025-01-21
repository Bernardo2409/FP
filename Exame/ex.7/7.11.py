with open('ex.7/vendas.txt', 'r', encoding='utf-8')as f:
    for line in f:
        lista = line.strip('/n').split(' ')
        valor = lista[4]
        num = ''.join([char for char in valor if char.isdigit() or char == '.'])
        texto = ''.join([char for char in valor if char.isalpha()])
        print(f"Venda a Dinheiro No {lista[0]}")
        print('-----------------------------')
        print(f"Empresa: {lista[1]}")
        print(f"N.C.: {lista[2]}")
        print(f"Data: {lista[3]}")
        print(f"Data: {num} {texto}")
        