
import random
N = int(input("Numero de vezes que o dado foi lançado"))
par = 0
for _ in range(N):
    numero = random.randint(1,6)
    if numero%2 ==0: par+=1
print(par)