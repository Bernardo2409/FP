import math
seno = 0
angulo = float(input())
parcelas = int(input())

for i in range(parcelas):
    soma = ((-1)**i)* (angulo ** (2*i+1)) / math.factorial(2 * i +1)
    seno += soma

print(f"O seno é aproximadamente {seno}")