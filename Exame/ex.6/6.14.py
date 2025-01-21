dic = {123123: ['M',18,176,55], 122222:['F',20, 260,40]}
novodict = {}
for key,i in dic.items():
    if i[0] =='M':
        novodict[key] = 66+(6.3* i[3])+ (12.9 * i[2]) - (6.8 * i[1])
    else:
        novodict[key] = 65.6+(4.3* i[3])+ (4.7 * i[2]) - (4.7 * i[1])
print(novodict)
