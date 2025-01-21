def exponencial(x,n):
    if n == 0:
        return 1
    if n%2 == 0:
        metade = exponencial(x,n//2)
        return metade * metade
    else:
        metade = exponencial(x,n//2)
        return metade*metade*x

print(exponencial(2,3))