import math
A = int(input("Cateto A?"))
B = int(input("Cateto B?"))
C = math.sqrt(pow(A,2) + pow(B,2))
print (C)
print (math.pi)
angle = math.acos(A/C) * 360 /(2* math.pi)
print(angle)