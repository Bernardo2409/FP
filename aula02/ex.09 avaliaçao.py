CTP = float (input ("Nota de CTP? "))
CP = float (input (" Nota de CP? "))


nota_minima = 6.5
nota_final = round (0.3 * CTP + 0.7 * CP, 0)

if CP and CTP >= nota_minima:
    if nota_final >= 10: print("Passaste")
    else: 
        print("Reprovado por nota final")
        ATPR = float (input("Nota ATPR? "))
        APR = float (input("Nota de APR? "))
        nota_recurso = round(0.3 * ATPR + 0.7 * APR)

        if nota_recurso >= 10 : print("Parabéns passaste")
        else : print("Chumbaste")
else :
  nota_final = 66
  print("Reprovado por nota mínima. A tua nota final é:", nota_final)
  ATPR = float (input("Nota ATPR? "))
  APR = float (input("Nota de APR? "))

  nota_recurso = round(0.3 * ATPR + 0.7 * APR)
  if nota_recurso >= 10 : print("Parabéns passaste")
  else: print("Chumbaste")
  