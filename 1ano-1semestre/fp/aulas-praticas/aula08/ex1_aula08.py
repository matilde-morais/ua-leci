# Aula de revisões

# Exercício 2

with open(names.txt, 'r') as arquivo: # Abre o arquivo em modo de leitura
    nomesCompletos = arquivo.readlines() # Lê todas as linhas do arquivo e armazena em uma lista de todos os nomes completos

primeiroUltimo = []
for linha in nomesCompletos:
    primeiroUltimo.append(([0],[-1])) # Adiciona na lista primeiroUltimo o primeiro e o último nome de cada linha

dicNomes = {}
for (primeiro, ultimo) in primeiroUltimo:
    if ultimo not in dicNomes:
        dicNomes[ultimo] = primeiro
    else: # Se o último nome já estiver no dicionário como chave, adiciona o primeiro nome na lista
        dicNomes[ultimo] += primeiro

print(dicNomes)