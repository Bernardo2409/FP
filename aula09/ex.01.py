
contador={}
with open("D:/UA/1ano/FP/aula07/examples/pg3333.txt",'r',encoding="utf-8") as f:
    text = f.read().lower()
    for char in text:
        if char.isalpha():
            if char in contador:
                contador[char] += 1
            else:
                contador[char] = 1
    for letra in sorted(contador, key=contador.get, reverse = False):
        print(f"{letra}: {contador[letra]}")
        