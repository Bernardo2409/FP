def removedup(s,i=0):
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return removedup(s[1:])
    else: 
        return s[0]+removedup(s[1:])
    
print(removedup('narrativss'))
    