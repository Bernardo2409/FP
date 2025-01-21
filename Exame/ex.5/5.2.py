A1 = [0.15, 6.52]
A20 = [0.12, 15.2]
A21 = [0.10, 5.75]
estrada = input()
if estrada == "A1":
    custo_por_km, custo_fixo = A1
elif estrada == "A20":
    custo_por_km, custo_fixo = A20
else:
    custo_por_km, custo_fixo = A21
custo_total = 120*custo_por_km + custo_fixo
print(f"O custo total é {custo_total:.2f}")