with open('D:/UA/1ano/FP/aula08/names.txt','r',encoding='utf-8') as f:
    lista=[]
    dicionario = {}
    for line in f:
        x=line.strip('\n').split(' ')
        if len(x) > 2:
            if x[-1] in dicionario:
                dicionario[x[-1]].add(x[0])
            else: 
                lista.append(x[-1])
                dicionario[x[-1]] ={x[0]}
    
    for key, value in dicionario.items():
        print(f"{key} : {value}")
        


