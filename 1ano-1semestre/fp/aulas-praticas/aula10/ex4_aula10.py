"""
Dada uma string, construa e devolva uma nova string onde
todas as letras 'x' apareçam movidas para o fim da string.
A função tem de ser recursiva. Não pode usar ciclos.

Given a string, return a new string where all the 
'x' chars have been moved to the end of the string.
The function must be recursive. You cannot use loops.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("hixhix") → "hihixx"
"""

def endX(s):

    # se a string estiver vazia, retorne a própria string
    if not s:
        return s
    
    # se o primeiro caracter for 'x', move-o para o final
    if s[0] == 'x':
        return endX(s[1:]) + 'x'
    # se não for 'x', mantém o caracter no início e processa o restante da string
    else:
        return s[0] + endX(s[1:])