# Devolve o número de linhas da matriz M.
def matrows(M):
   return len(M)

# Complete para devolver o número de colunas da matriz M.
def matcols(M):
    return len(M[0])

# Complete a função para devolver uma matriz com m×n zeros.
def matzeros(m, n):
    M = [[0] * n for _ in range(m)]
    return M

def matzerosTEST(m, n):
   M = matzeros(m, n)
   M[0][1] = 1   # should change just 1 element!
   return M

# Complete a função para multiplicar a matriz A pela matriz B.
def matmult(A, B):
    assert matcols(A) == matrows(B)
    
    mA = matrows(A)
    mB = matrows(B)
    nA = matcols(A)
    nB = matcols(B)

    C = [[0] * nB for _ in range(mA)]

    for i in range(mA):
        for j in range(nB):
            for k in range(mB):
                C[i][j] += A[i][k] * B[k][j]

    return C

def matmultTEST(A, B):
   C = matmult(A, B)
   return A, B, C