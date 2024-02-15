# Aula TP 13

import time
import os

# Exercíco 1
# Uma função que receba o nome do ficheiro e devolva uma lista de túpulos, em que cada
# túpulo terá a informação correspondente a uma linha (informação de um clube).

def tupulos(fileName):
  tupulos = []
  with open(fileName, 'r') as csvFile:
    for line in csvFile:
      lineSeparated = line.strip().split(',')
      position = lineSeparated[0]
      name = lineSeparated[1]
      country = lineSeparated[2]
      actualScore = lineSeparated[3]
      changePosition = lineSeparated[4]
      LastScore = lineSeparated[5]
      downUp = lineSeparated[6]
      tupulo = (position, name, country, actualScore, changePosition, LastScore, downUp)
      print(tupulo)
      tupulos.append(tupulo)
  return tupulos

# Exercício 2
# 2 - Uma função que receba como argumento o nome de um país e que imprima no ecrã os
# clubes desse país, o número respetivo no ranking e o score atual.

def clubesPais(fileName, pais):
  clubesPais = []
  with open(fileName, 'r') as csvFile:
    for line in csvFile:
      lineSeparated = line.strip().split(',')
      position = lineSeparated[0]
      name = lineSeparated[1]
      country = lineSeparated[2]
      actualScore = lineSeparated[3]

      if country == pais:
        print(f"{name},{position},{actualScore}")
        tuplo = (name, position, actualScore)
        clubesPais.append(tuplo)
  return clubesPais

# Exercício 3
# Uma função com base na anterior que receba também o nome de um ficheiro de output e
# que escreva nesse ficheiro a informação impressa no ecrã da alínea anterior.

def output(fileName, pais, outputFile):
  clubesPais = []
  with open(fileName, 'r') as csvFile:
    for line in csvFile:
      lineSeparated = line.strip().split(',')
      position = lineSeparated[0]
      name = lineSeparated[1]
      country = lineSeparated[2]
      actualScore = lineSeparated[3]

      if country == pais:
        tuplo = (name, position, actualScore)
        clubesPais.append(tuplo)

  with open(outputFile, 'w') as outputFile:
    for tuplo in clubesPais:
      outputFile.write(f"{tuplo[0]},{tuplo[1]},{tuplo[2]}")
      
  return clubesPais

# Exercício 4
# Uma função que receba a lista de túpulos e que devolva um dicionário em que a chave é o
# país sede dos clubes e o valor correspondente deverá ser uma lista com o nome de todos os
# clubes desse país.

def dicionario(fileName):
  tupulos = tupulos(fileName)
  dicionario = {}
  for tupulo in tupulos:
    country = tupulo[2]
    if country in dicionario.keys():
      dicionario[country].append(tupulo[1])
    else:
      dicionario[country] = [tupulo[1]]
  print(dicionario)
  return dicionario

# Exercício 5
# Uma função que receba a lista de túpulos e devolva o túpulo correspondente ao clube que
# mais subiu no ranking.

def maisSubiu(fileName):

  tupulos = tupulos(fileName)
  subiram = []
  changed = []

  for tupulo in tupulos:
    if tupulo[6] == '+':
      subiram.append(tupulo)
      changed.append(tupulo[4])

  indexMaxChanged = changed.index(max(changed))
  
  print(f"O clube que mais subiu no ranking foi {subiram[indexMaxChanged][1]}.")
  return subiram[indexMaxChanged]

# Exercício 6
# Uma função que receba o nome de um clube e que imprima no ecrã os dados desse clube se
# este existir e uma mensagem de erro nos restantes casos.

def information(fileName, name):
  tupulos = tupulos(fileName)
  for tupulo in tupulos:
    if (tupulo[1]).lower() == name.lower():
      print(f"{tupulo[0]},{tupulo[1]},{tupulo[2]},{tupulo[3]},{tupulo[4]},{tupulo[5]},{tupulo[6]}")
    else:
      print("Clube não encontrado! Tente outra vez.")

# Exercício 7
# Uma função que determine o ranking médio de cada um dos países e o apresente no ecrã (o
# ranking médio determina-se somando o ranking de todos os clubes de um dado país e dividindo
# pelo número de clubes desse país.
      
# Exercício 8 
# Altere a função anterior de forma a que imprima os países por ordem crescente do ranking
# médio obtido.

def rankingMedio(fileName):
  dicionario = dicionario(fileName)
  tupulos = tupulos(fileName)
  rankingMedioList = []
  for pais in dicionario.keys():
    soma = 0
    numeroClubes = 0
    for tupulo in tupulos:
      if tupulo[2] == pais:
        soma += int(tupulo[3])
        numeroClubes += 1
    rankingMedio = soma / numeroClubes
    rankingMedioList.append((pais, rankingMedio))
  rankingMedioList.sort(key=lambda x: x[1])
  print(rankingMedioList)
  return rankingMedioList

# Exercício 9
# Desenvolva ainda uma função que apresente um menu com as diferentes opções
# desenvolvidas nas alíneas anteriores e que as permita testar. A opção 0 permitirá abandonar o
# programa, em todas as restantes opções após a chamada da função respetiva deverá ser
# apresentado de novo o menu e deverá ser possível escolher outra opção.

def menu(fileName, outputFile):
  print("1 - Ler o ficheiro e devolver tuplos")
  print("2 - Clubes de um país")
  print("3 - Dicionário de clubes por país")
  print("4 - O que que mais subiu no ranking")
  print("5 - Informação sobre um clube")
  print("6 - Ranking médio por país")
  print("0 - Sair")

  option = input("Escolha uma opção: ")

  if option == "1":
    os.system('clear')
    tupulos(fileName)
    print("\n\n\n\n")
    time.sleep(3)
    menu(fileName, outputFile)
  elif option == "2":
    os.system('clear')
    pais = input("Escolha um país: ")
    clubesPais(fileName, pais)
    print("\n\n")
    opcao = input("Deseja guardar a informação num ficheiro? (s/n): ")
    if opcao == "s":
      output(fileName, pais, outputFile)
      print("")
      print("Já está!")
    elif opcao == "n":
      print("")
      print("Ok!")
    print("\n\n\n\n")
    time.sleep(3)
    menu(fileName, outputFile)
  elif option == "3":
    os.system('clear')
    dicionario(fileName)
    print("\n\n\n\n")
    time.sleep(3)
    menu(fileName, outputFile)
  elif option == "4":
    os.system('clear')
    maisSubiu(fileName)
    print("\n\n\n\n")
    time.sleep(3)
    menu(fileName, outputFile)
  elif option == "5":
    os.system('clear')
    name = input("Escolha um clube: ")
    information(fileName, name)
    print("\n\n\n\n")
    time.sleep(3)
    menu(fileName, outputFile)
  elif option == "6":
    os.system('clear')
    rankingMedio(fileName)
    print("\n\n\n\n")
    time.sleep(3)
    menu(fileName, outputFile)
  elif option == "0":
    os.system('clear')
    print("Até à próxima!")
  else:
    os.system('clear')
    print("Opção inválida! Escolha uma opção do menu.")
    time.sleep(3)
    menu(fileName, outputFile)

def main():
  print("Bem-vindo ao Soccer Football Clubs Ranking!")
  print("\n\n")
  fileName = 'Soccer_Football_Clubs_Ranking.csv'
  outputFile = 'output.csv'
  menu(fileName, outputFile)

if __name__ == "__main__":
  main()