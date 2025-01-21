with open('ex.7\primeiro.txt','r', encoding='utf-8') as f:
    lista=[]
    for line in f:
        line = line.strip('\n').split(' ')
        for i in line:
            try:
                lista.append(float(i))
            except ValueError:
                pass
    print(lista)