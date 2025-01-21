autor = {"php":"Rasmus Lerdorf","perl":"Larry Wall","tcl":"John Ousterhout",
"awk":"Brian Kernighan","java":"James Gosling","parrot":"Simon Cozens",
"python":"GuidovanRossum","xpto":"zxcv"}

autor['preço certo']='Gordo'
autor['python'] = 'Guido Van Rossum'
autor.pop("xpto")
numero = len(autor)
print(autor)
print(numero)
if "c++" in autor:
    print('true')
else:
    print("false")