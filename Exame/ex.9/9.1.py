def resto(dividendo, divisor):
    if dividendo >= divisor:
        return resto(dividendo-divisor,divisor) 
    else: return dividendo



print(resto(30,3))