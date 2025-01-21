dias_semana = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta', 5:'Quinta',6:'Sexta',7:'Sabado'}
meses_ano = {1:'Janeiro',2:'Fevereiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
s ='4/5/6/2006'
lista = list(map(int,s.split('/')))
print(f"{dias_semana[lista[0]]}, {lista[1]} de {meses_ano[lista[2]]} de {lista[3]}")

