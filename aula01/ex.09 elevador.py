M = int(input("Moradores por andar? "))
A = int(input("Andares do prédio? "))
print("número de andares", A)


soma_andares =  A * (A+1) /2  #Quantos andares passa o elevador
distancia_diaria = 3 * M * soma_andares *4


print ("Distância diária do elevador", distancia_diaria)


distance_year = distancia_diaria * 365 /100
print ("Distancia ao ano ", distance_year, "kms")

time = distance_year * 100 /3600
print(time, "horas")

