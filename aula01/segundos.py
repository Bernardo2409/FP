seg = int(input ("Segundos?"))
horas = seg // 3600

resto = seg % 3600

minutos = resto // 60
segundos = resto % 60


print("{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))
