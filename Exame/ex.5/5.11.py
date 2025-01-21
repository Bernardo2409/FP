fatorial = int(input())
resultado = 1
for i in range(fatorial):
    resultado *= (fatorial-i)
print(resultado)
