def produto_escalar(v,w,i=0):

    if i == len(v):
        return 0
    else:
        return v[i]*w[i]+produto_escalar(v,w,i+1)
print(produto_escalar((1,2,3),(1,1,1)))