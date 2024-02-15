# Aulas de revisão

# Preparação antes da aula 1

L1 = [1, 3, 5, 7, 9]
[10+x for x in L1] # L1 = [11, 13, 15. 17, 19]
L2 = [2, 4, 6]
[x+y for x in L1 for y in L2] # L1 = [3, 5, 7, 5, 7, 9, 7, 9, 11, 9, 11, 13, 11, 13, 15]
{x+y for x in L1 for y in L2} # L1 = {3, 5, 7, 9, 11, 13, 15} retira os repetidos
[(x,y) for x in L1 for y in L2] # L1 = [(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6), (5, 2), (5, 4), (5, 6), (7, 2), (7, 4), (7, 6), (9, 2), (9, 4), (9, 6)]
[(x,y) for y in L2 for x in L1] # L2 = [(2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9), (6, 1), (6, 3), (6, 5), (6, 7), (6, 9)]
[x*c for c in "abc" for x in L1] # L1 = [ 'a', 'aaa', 'aaaaa', 'aaaaaaa', 'aaaaaaaaa', 'b', 'bbb', 'bbbbbb', 'bbbbbbbb', 'bbbbbbbbbb', 'c', 'ccc', 'cccccc', 'cccccccc', 'cccccccccc' ]

# Correto!

# Preparação antes da aula 2

[x%3==0 for x in L1] # L1 = [False, True, False, False, True]
[(x,x//3) for x in L1 if x%3==0] # Apenas vamos considerar o 3 e o 9. L1 = [(3, 1), (9, 3)]
{x:x//3 for x in L1 if x%3==0} # Apenas vamos considerar o 3 e o 9. Criar um dicionário. L1 = {3: 1, 9: 3}
[(x,y) for x in L1 for y in L2 if x<y]
# L1 = [(1, 2), (1, 4), (1, 6), (3, 4), (3, 6), (5, 6)]
{ x:[y for y in L2 if x<y] for x in L1 }
# Criar um dicionário. L1 = {1:[2, 4, 6], 3:[4, 6], 5:6}
any(x%2==0 for x in L1)
# any() verifica se algum elemento é verdadeiro, e se for, retorna True.
# L1 = False

# Correto!