import os # módulo que fornece uma interface para interagir com o sistema operacional (até certo ponto)

dirList = [] # lista de tudo o que está dentro do diretório principal que queremos analisar

def printDirFiles(d):
    lst = os.listdir(d) # os.listdir(): retorna uma lista com os nomes dos ficheiros e subdiretórios num determinado diretório
    
    # Itera sobre cada item na lista
    for fname in lst:
        path = os.path.join(d, fname) # os.path.join(): concatena componentes de caminho em um caminho completo

        if os.path.isfile(path): # os.path.isfile(): verifica se um caminho corresponde a um ficheiro
            ftype = "FILE"
            dirList.append((fname, ftype, path))
        elif os.path.isdir(path): # os.path.isdir(): verifica se um caminho corresponde a um diretório
            ftype = "DIR"
            dirList.append((fname, ftype, path))
            printDirFiles(path) # recursividade: repete a função para o diretório encontrado
        else: # caso não seja um ficheiro ou um diretório
            ftype = "?"
            dirList.append((fname, ftype, path))

        # imprime o nome, tipo (FILE, DIR ou ?) e o caminho do item
        print(fname, ftype, path)
    return

def findFiles(path, ext): # função para encontrar ficheiros com uma extensão específica
    
    extList = [] # lista de ficheiros com uma extensão específica

    for item in dirList: # itera sobre cada item na lista de itens do diretório principal
        if item[1] == "FILE" and item[0].endswith(ext): # se ftype = "FILE" *e* fname termina com a extensão específica
            # .endswith() verifica se uma string termina com um sufixo específico, dá True se sim e False se não
            extList.append(item[2])
    return extList

def main():

    dirList.clear()  # Limpa a lista antes de cada execução

    print("\nTesting printDirFiles('..'):\n")
    printDirFiles("..") # ".." é o diretório acima do diretório atual

    print("\nTesting findFiles('..', '.py'):\n")
    extList = findFiles("..", ".py") # chama a função findFiles() para encontrar ficheiros com a extensão .py
    print(extList)
    assert isinstance(extList, list) # assert é usado para verificar se uma determinada condição é verdadeira, se sim, o programa continua, se não, uma exceção do tipo AssertionError é levantada, interrompendo o programa
    # a condição acima verifica se o resultado da função findFiles() é uma lista

    print("\nTesting findFiles('..', '.csv'):\n")
    extList2 = findFiles("..", ".csv") # chama a função findFiles() para encontrar ficheiros com a extensão .csv
    print(extList2)
    assert isinstance(extList2, list)

if __name__ == "__main__":
    main()