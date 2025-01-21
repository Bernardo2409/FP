# Este programa demonstra a leitura e utilização de dados de um ficheiro JSON
# com mensagens do Twitter.
# Modifique-o para resolver o problema proposto.


# O módulo json permite descodificar ficheiros no formato JSON.
# São ficheiros de texto que armazenam objetos compostos que podem incluir
# números, strings, listas e/ou dicionários.
import json

from collections import Counter

# Abre o ficheiro e descodifica-o criando o objeto twits.
with open("twitter.json", encoding="utf8") as f:
    twits = json.load(f)

# Analise os resultados impressos para perceber a estrutura dos dados.
print(type(twits))       # deve indicar que é uma lista!
print(type(twits[0]))    # cada elemento da lista é um dicionário.
print(twits[0].keys())   # mostra as chaves no primeiro elemento.

# Cada elemento contém uma mensagem associada à chave "text":
print(twits[0]["text"])

# Algumas mensagens contêm hashtags:
print(twits[880]["text"])

def palavras(twits):
    lista=[]
    for dic in twits:
        texto=dic["text"]
        words=texto.split()
        for i in words:
            lista.append(i)
    return lista
lista = palavras(twits)

def order(lista):
    listaord=[item for items, c in Counter(lista).most_common() for item in [items] * c]
    return listaord
listaord=order(lista) 


def hashtags(listaord):
    hashtagslist=[]
    for word in listaord:
        if word[0]=="#":
            hashtagslist.append(word)
    return hashtagslist

hashtagslist=hashtags(listaord)

def dicionario(hashtagslist):
    dic={}
    c=0
    for i in hashtagslist: # cria um dicionario com o numero de vezes que aparece cada palavra
         if i not in dic.keys():
            dic[i]=1
         else:
            c+=1
            dic[i]=c
    return dic

dic=dicionario(hashtagslist)
print(dic)

def popular(dic):
    d=0
    #print(dic.items)
    dicts={key: val for key, val in sorted(dic.items(), key = lambda a: a[1], reverse = True)} #dicionario, por ordem decrescente, das palavras mais repetidas
    i=1
    for f in dicts.values():
        if i>1:
            break
        p=f
        i=2
        
    for key in dicts:
        if d <10:
            d+=1
            r=round(18*dicts[key]/p) #ratio
            print("{}{:>35}{}".format((key),dicts[key],r*"+"))
popular(dic)