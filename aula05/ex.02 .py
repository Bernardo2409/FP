def inputFloatlist():
    l = []
    s = 1
    while s != "":
        s = input("Insere um float, quando quiseres encerrar dá enter")
        if s != "":
            l.append(float(s))
    l.pop()
    return l

def countLower(lst,v):
    counter = 0
    for s in lst:
        if float(s) < v:
            counter += 1
    print(counter)
    return counter

def minmax(lst):
    min_val = lst[0]
    max_val = lst[0]

    for n in lst[1:]:
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n
    print (min_val, max_val)
    return min_val, max_val        

def main():
    l = inputFloatlist()
    print (l)

    min_val, max_val = minmax(l)
    n = (min_val + max_val) / 2
    print(n)
    countLower(l,n)
    minmax(l)
main()





