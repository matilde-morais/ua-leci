# Recursividade - Explicação

# VERSÃO SEM RECURSIVIDADE
def fatorial (n)
    res = 1
    if n == 0 or n == 1: # se o nº for 0 ou 1
        return 1 # então o resultado do fatorial é 1
    else:
        for x in range (2, n - 1): # vai fazendo o fatorial
            res *= x

# VERSÃO COM RECURSIVIDADE
def fatorial_recursivo (n)
    if n == 0 or n == 1: # se o nº for 0 ou 1
        return 1 # então o resultado do fatorial é 1
    else:
        return n * fatorial_recursivo(n-1)
    
        # se n = 4:
        
        # 4 != o e 1, portanto continua
        # 4 * fatorial_recursivo(3)
        # 3 != o e 1, portanto continua
        # 3 * fatorial_recursivo(2)
        # 2 != o e 1, portanto continua
        # 2 * fatorial_recursivo(1)
        # 1 == 1
        # return 1

        # 2*1 = 2
        # 3*2 = 6
        # 4*6 = 24
        
        # fatorial_recursivo(4) = 24