hora = int(input("Horas?"))
minuto = int(input("Minutos?"))
segundo = int(input("Segundos?"))

tempo_segundos = (hora *3600) + (minuto * 60) + segundo

print(tempo_segundos)

hra = (tempo_segundos //3600)
h = format(hra)
print (h)




