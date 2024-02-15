# Escreva um programa que determine a frequência de ocorrência de todas as letras que
# ocorrem num ficheiro de texto. (Pode usar c.isalpha() para verificar se um caráter
# c é uma letra). O nome do ficheiro deve ser passado como argumento na linha de
# comando (use sys.argv). Descarregue “Os Lusíadas” (documento 3333 do Projeto
# Gutenberg) e faça a contagem. Ajuste o programa para não distinguir maiúsculas de
# minúsculas. (Pode usar s.lower() para converter uma string s para minúsculas.)
# Finalmente, modifique o programa para mostrar o resultado por ordem alfabética.

import sys  # Importa o módulo sys para acessar argumentos da linha de comando
import time  # Importa o módulo time para utilizar a função sleep

def count_letters(filename): # Função que conta as letras

    file = open(filename, 'r') # Abre o ficheiro
    text = file.read() # Lê o ficheiro e guarda o conteúdo na variável text
    file.close() # Fecha o ficheiro
    
    letters = {} # Começamos com uma lista vazia
    for letter in text: # Vai correr todas as letras no texto
        if letter.isalpha(): # Apenas se foram letras
            letter = letter.lower() # Toran qualquer tipo de letra em minúscula
            if letter in letters: # Caso a letra a ser analisada já esteja na lista de contagem de letras
                letters[letter] += 1
            else: # Caso a letra a ser analisada não esteja ainda na lista de contagem de letras
                letters[letter] = 1
    return letters # Devolve a lista

def sorted_alphabetically(letters): # Função que ordena a lista alafabeticamente
    return sorted(letters.items())  # Retorna as letras ordenadas em ordem alfabética, incluindo a contagem delas, em tuples

def main(): #Função principal

    if len(sys.argv) < 2:  # Verifica se o nome do ficheiro foi passado como argumento
        print("Por favor, indique  o nome do ficheiro que quer analisar como argumento.")
        sys.exit(1)  # Encerra o programa com código de saída 1 (indicando um erro)

    filename = sys.argv[1]  # Obtém o nome do ficheiro do argumento passado

    print("Vamos começar a contagem de cada letra do seu ficheiro.\n")
    time.sleep(5)

    letters = count_letters(filename)  # Chama a função count_letters

    print("Aqui está a contagem de cada letra do seu ficheiro, por ordem alfabética:\n")

    sorted_letters = sorted_alphabetically(letters)  # Chama a função sorted_alphabetically

    for letter, count in sorted_letters:
        print(f"Letra: {letter}, Contagem: {count}")  # Imprime cada letra e a sua contagem, já na ordem alfabética

main()  # Chama a função principal se o script for executado diretamente
