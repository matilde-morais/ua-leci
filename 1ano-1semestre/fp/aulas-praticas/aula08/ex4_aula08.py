# Aula de revisões

# Exercicio 3

# devolve conjunto de todos os nºs primos até n
def primesUpTo(n):
    if n < 2: # Se n é menor que 2
        return []  # Não há números primos menores que 2

    primes = [2]  # Se n é 2 ou maior, o primeiro primo é 2
    
    # Itera pelos nºs de 3 até n, de 2 em 2 (apenas ímpares)
    for i in range(3, n + 1, 2):
        is_prime = True
        # Verifica se i é divisível por algum número primo existente em na lista primes
        for prime in primes:
            if prime > int(i**0.5) + 1:  # Se prime^2 > i, não há necessidade de verificar mais
                break
            if i % prime == 0:  # Se i é divisível por prime, então i não é primo
                is_prime = False
                break
        
        # Se is_prime for True, i é primo e é adicionado à lista 'primes'
        if is_prime:
            primes.append(i)

    return primes

print(primesUpTo(15)) # A solução deve ser: [2, 3, 5, 7, 11, 13]