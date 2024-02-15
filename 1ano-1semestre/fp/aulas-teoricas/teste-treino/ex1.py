# NMEC: 118866

"""
A sequência de Fibonacci começa com os números 0 e 1.  Depois, cada elemento
consecutivo da sequência obtém-se pela soma dos dois elementos anteriores.
Complete a função genFibonacci(n) para _devolver_ uma lista com os n primeiros
números de Fibonacci.  Por exemplo, se n=6, deve devolver [0, 1, 1, 2, 3, 5].
A função só tem de funcionar para n>=2.

The Fibonacci sequence starts with the numbers 0 and 1. Then each consecutive
element of the sequence is obtained by the sum of the two previous elements.
Complete the genFibonacci(n) function to _return_ a list of the first n
Fibonacci numbers. For example, if n=6, it should return [0, 1, 1, 2, 3, 5].
The function only has to work for n>=2.
"""

def genFibonacci(n):
   assert n >= 2
   
   a = 0
   b = 1
   
   lst = [0, 1]
   
   while not len(lst) == n:
      c = a + b
      lst.append(c)
      a = b
      b = c
   return lst
      
      
      

   

# NÃO precisa de invocar a função.  O codecheck trata disso.
# You DO NOT need to call the function.  Codecheck does that for you.