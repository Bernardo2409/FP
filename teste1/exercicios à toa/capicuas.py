def tamanho_capicua_mais_longa(s):
    tamanho_max = 0

    for i in range(len(s)):
        for tipo in [0, 1]:  # 0 para capicua ímpar, 1 para capicua par
            esq, dir = i, i + tipo
            while esq >= 0 and dir < len(s) and s[esq] == s[dir]:
                esq -= 1
                dir += 1
            tamanho_max = max(tamanho_max, dir - esq - 1)

    return tamanho_max
print(tamanho_capicua_mais_longa("1"))       # 1
print(tamanho_capicua_mais_longa("12"))      # 1
print(tamanho_capicua_mais_longa("323"))     # 3
print(tamanho_capicua_mais_longa("74989"))   # 3
print(tamanho_capicua_mais_longa("11"))      # 2