import math
numero = int(input())
if numero > 1:
    for i in range(2,numero+1):
        if numero % i == 0:
                divisor = i
                break
        

print(divisor)

