time= int(input("tempo de chamada em segundos"))
minutos = time / 60

if time <= 60: money = 0.12
else: money = 0.12 + 0.12 * (minutos- 1)

print(money)