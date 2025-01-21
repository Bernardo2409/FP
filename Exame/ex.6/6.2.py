lst = [1,4,7,9,3,2,8,5,6]

pares = sum([x for x in lst if x%2 ==0])
impares = sum([x for x in lst if x%2!=0])
print((pares, impares))
