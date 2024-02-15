# O programa telefone.py simula a lista de contactos de um telemóvel, implementada
# com um dicionário. O programa apresenta um menu com cinco operações. A operação
# “Listar contactos” já está implementada. Experimente e analise o programa.
# a) Acrescente a operação de “Adicionar contacto”. Deve pedir um número e nome, e
# acrescentá-los ao dicionário.
# b) Acrescente a operação de “Remover contacto”. Deve pedir o número e eliminar o
# item correspondente. (Use o operador del ou o método pop.)
# c) Acrescente a operação “Procurar Número”. Deve pedir um número e mostrar o nome
# correspondente, se existir, ou o próprio número, caso contrário. Sugestão: pode
# recorrer ao método get. Repare que o dicionário permite uma solução mais simples
# e eficiente do que a solução que fez em aula05/telephones.py.
# d) Complete a função filterPartName, que dada uma string, deve devolver um
# dicionário com os contactos {número: nome} cujos nomes incluam essa string. Use
# essa função para implementar a operação “Procurar Parte do nome”, que deve pedir
# um nome parcial e listar os contactos que o contêm. Aqui tem de fazer uma solução
# análoga à da função nameToTels de aula05/telephones.py.

# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    ...


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()