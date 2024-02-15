# Projeto 2 - Fundamentos de Programação

'''
Necessário fazer a instalação do módulo requests:

LINUX:
sudo apt install python3-pip
pip3 install requests

WINDOWS:
pip install requests
'''

'''
Necessário fazer a instalação da biblioteca timezonefinder:

LINUX:
sudo apt install python3-pip
pip3 install timezonefinder

WINDOWS:
pip install timezonefinder
'''

import requests 
# importar o módulo requests. este é utilizado para enviar requisições HTTP e obter respostas de servidores web.
import json 
# importar o módulo json. este módulo é usado para codificar e descodificar dados no formato JSON (JavaScript Object Notation), facilitando a troca de informações estruturadas entre sistemas.
import time
# importar o módulo time. este módulo fornece várias funções relacionadas ao tempo.
import os
# importar o módulo os. este módulo fornece funções para interagir com o sistema operacional.
import csv
# importar o módulo csv. este módulo fornece funções para ler e escrever dados em ficheiros CSV (Comma-Separated Values).
from timezonefinder import TimezoneFinder
# da biblioteca timezonefinder, importar a classe TimezoneFinder. esta classe é usada para obter o fuso horário de uma localização geográfica.




# Parte 1. Ler o ficheiro categories.txt e armazenar as categorias:


'''
O ficheiro categories.txt tem de estar na mesma pasta que o ficheiro projeto2.py
'''

# função para ler o ficheiro categories.txt e armazenar as categorias numa lista
def readCategories():
    try: # tenta executar o código abaixo
        with open('categories.txt', 'r') as file: # com o 'with open' não é necessário fechar o ficheiro
            categories = [line.strip() for line in file] # .strip() remove os espaços em branco no início e no fim da string. é criada uma lista com as novas linhas
        return categories # devolve a lista de categorias
    except FileNotFoundError: # se o ficheiro não for encontrado
        print("Erro: O arquivo categories.txt não foi encontrado.")
        return [] # devolve uma lista vazia


# Parte 2. Pedir informações básicas ao utilizador:


# função para obter a latitude
def getLatitude():
    while True: # enquanto o utilizador não introduzir um valor correto
        try: # tenta executar o código abaixo
            latitude = float(input("\nIntroduza a latitude de partida: ")) # receber a latitude de partida do utilizador, em float
            return latitude # devolve a latitude, em float
        except ValueError: # se o utilizador introduzir um valor que não é um float
            print('Introduza um valor correto (inteiro ou decimal)!)')

# função para obter a longitude
def getLongitude():
    while True: # enquanto o utilizador não introduzir um valor correto
        try: # tenta executar o código abaixo
            longitude = float(input("\nIntroduza a longitude de partida: ")) # receber a longitude de partida do utilizador, em float
            return longitude # devolve a longitude, em float
        except ValueError: # se o utilizador introduzir um valor que não é um float
            print('Introduza um valor correto (inteiro ou decimal)!')

# função para obter o raio máximo de distância
def getDistance():
    while True: # enquanto o utilizador não introduzir um valor correto
        try: # tenta executar o código abaixo
            distance = float(input("\nIntroduza a distância máxima que pretende viajar, em km: ")) # receber a distância máxima, em km, do utilizador, em float
            return distance # devolve a distância, em float
        except ValueError: # se o utilizador introduzir um valor que não é um float
            print('Introduza um valor correto (inteiro ou decimal e em km)!')

# função para obter informações, como a latitude, longitude, distância máxima e tipos de atrações, do utilizador
def getInformation():

    latitude = getLatitude() # obtém a latitude
    longitude = getLongitude() # obtém a longitude
    maxDistance = getDistance() # obtém a distância máxima
    typesAttraction = input("\nIntroduza os tipos de atrações que deseja visitar (separados por vírgula), em inglês (exemplo: catering,accommodation): ").split(',') # receberá uma lista dos tipos de atrações que o utilizador deseja visitar, com cada item dividido por vírgula

    # validar os tipos de atrações, dados pelo utilizador, com base nas categorias lidas no fichero categories.txt
    categories = readCategories() # chamada da função readCategories()
    typesAttraction = [tipo.strip() for tipo in typesAttraction if tipo.strip() in categories] # a lista typesAttraction será alterada para conter apenas os tipos de atrações que estão também na lista categories

    return latitude, longitude, maxDistance, typesAttraction # devolve a latitude, longitude, distância máxima e tipos de atrações, em float e lista

# função para obter o fuso horário de uma localização geográfica
def getTimezone(latitude, longitude):
    try: # tenta executar o código abaixo
        tf = TimezoneFinder() # cria um objeto TimezoneFinder
        timezoneStr = tf.timezone_at(lng=longitude, lat=latitude) # obtém o fuso horário da localização geográfica, dada pela latitude e longitude, em string
        return timezoneStr # devolve o fuso horário
    except Exception as e: # se houver um erro ao obter o fuso horário
        print(f"Erro a obter o Fuso Horário: {e}") # imprime o erro
        return 'N/A' # devolve 'N/A'


# Parte 3. Obter informações das APIs:


# função para obter as atrações disponíveis, com base na latitude, longitude, distância máxima e tipos de atrações dados pelo utilizador
def getAttractions(latitude, longitude, maxDistance, typesAttraction):
    try: # tenta executar o código abaixo
        apiKey = '1a48d55784ea45f09b69009f7eda2a31' # apikey para aceder à API
        endPoint = "https://api.geoapify.com/v2/places" # endpoint da API

        # Verifica se há tipos de atrações especificados
        if not typesAttraction: # se o utilizador não especificou nenhum tipo de atração
            print("Por favor, indique pelo menos um tipo de atração válida.")
            return None # devolve None

        params = { # parâmetros para a API
            'categories': ','.join(typesAttraction), # junta os tipos de atrações numa string, separados por vírgula, e atribui ao parâmetro 'categories'
            'lat': latitude, # atribui a latitude ao parâmetro 'lat'
            'lon': longitude, # atribui a longitude ao parâmetro 'lon'
            'radius': maxDistance, # atribui a distância máxima ao parâmetro 'radius'
            'apiKey': apiKey # atribui a apikey ao parâmetro 'apiKey'
        }

        response = requests.get(endPoint, params=params) # envia uma solicitação GET para o endpoint da API, com os parâmetros especificados (pedidos do utilizador)

        '''
        Tipos de códigos de status HTTP:
        200: OK
        201: Created
        204: No Content

        301: Moved Permanently
        302: Found
        307: Temporary Redirect

        400: Bad Request
        401: Unauthorized
        403: Forbidden
        404: Not Found

        500: Internal Server Error
        502: Bad Gateway
        503: Service Unavailable
        '''

        if response.status_code == 200: # se o código de status da resposta for 200 (OK)
            return response.json()['features'] # devolve as 'features' da resposta JSON
        else: # se o código de status da resposta não for 200
            print(f"Erro na solicitação à API. Código de status: {response.status_code}")
            print(response.text) # imprime o texto da resposta 
            return [] # devolve uma lista vazia
    except requests.RequestException as e: # se houver um erro na solicitação à API
        print(f"Erro na solicitação à API: {e}")
        return [] # devolve uma lista vazia

# função para obter a moeda de um país
def getCurrency(country):
    try: # tenta executar o código abaixo
        endpoint = f"https://restcountries.com/v3.1/name/{country}"

        response = requests.get(endpoint) # envia uma solicitação GET para o endpoint da API

        if response.status_code == 200: # se o código de status da resposta for 200 (OK)
            data = response.json() # devolve os dados da resposta JSON
            currencies = data[0].get('currencies', {}) # se a chave 'currencies' existir, atribui o seu valor à variável 'currencies'. se não existir, atribui um dicionário vazio.

            if currencies: # se houver moedas
                currencyName = list(currencies.keys())[0] # obtém o nome da moeda
                currencySymbol = currencies[currencyName].get('symbol', '') # se a chave 'symbol' existir, atribui o seu valor à variável 'currencySymbol'. se não existir, atribui uma string vazia.
                currency = f"{currencyName} ({currencySymbol})"
                return currency # devolve a moeda
            else: # se não houver moedas
                return "Moeda do país da atração não encontrada."
        else: # se o código de status da resposta não for 200
            return f"Erro ao obter informações do país. Código de status: {response.status_code}"
    except requests.RequestException as e: # se houver um erro na solicitação à API
        return f"Erro na solicitação à API de países: {e}"


# Parte 4. Processar, mostrar e guardar os resultados obtidos:


# função para mostrar as informações obtidas das APIs, consoante o pedido do utilizador
def showAttractions(attractions,maxDistance):
    count = 0 # contador para o nº de atrações válidas
    for attraction in attractions: # para cada atração na lista de atrações

        properties = attraction.get('properties', {}) # obtem as propriedades da atração
        distance = properties.get('distance', 'N/A') # se a chave 'distance' existir, atribui o seu valor à variável 'distance'. se não existir, atribui 'N/A'.
        
        if distance != 'N/A' and float(distance) <= (maxDistance * 1000): # se a distância for diferente de 'N/A' e menor ou igual à distância máxima
            
            geometry = attraction.get('geometry', {}) # obtem a geometria da atração

            name = properties.get('name', 'N/A') # se a chave 'name' existir, atribui o seu valor à variável 'name'. se não existir, atribui 'N/A'.

            if name != 'N/A': # se o nome da atração for diferente de 'N/A'
                attractionType = properties.get('categories', 'N/A')  # se a chave 'categories' existir, atribui o seu valor à variável 'attractionType'. se não existir, atribui 'N/A'.
                country = properties.get('country', 'N/A') # se a chave 'country' existir, atribui o seu valor à variável 'country'. se não existir, atribui 'N/A'.
                address = properties.get('formatted', 'N/A') # se a chave 'formatted' existir, atribui o seu valor à variável 'address'. se não existir, atribui 'N/A'.
                contact = properties.get('contact', 'N/A') # se a chave 'contact' existir, atribui o seu valor à variável 'contact'. se não existir, atribui 'N/A'.
                coordinates = geometry.get('coordinates', [0, 0]) # se a chave 'coordinates' existir, atribui o seu valor à variável 'coordinates'. se não existir, atribui as coordenadas [0, 0].
                latitude, longitude = coordinates if len(coordinates) == 2 else (0, 0) # se houver 2 coordenadas, atribui-as às variáveis 'latitude' e 'longitude'. se não houver, atribui 0 e 0.
                timezone = getTimezone(latitude, longitude) # chama a função getTimezone(), para obter o fuso horário da atração.
                currency = getCurrency(country) # chama a função getCurrency(), para obter a moeda do país da atração.

                print(f"\nTipo de Atração: {attractionType}\nNome: {name}\nPaís: {country}\nEndereço: {address}\nLocalização: ({latitude}, {longitude})\nContacto: {contact}\nDistância: {distance/1000} km\nFuso Horário: {timezone}\nMoeda: {currency}\n")
                count += 1 # incrementa o contador
    return count # devolve o nº de atrações válidas

# função para guardar as informações obtidas das APIs num ficheiro CSVPath
def exportToCSV(attractions, maxDistance):
    attractions.sort(key=lambda x: x.get('properties', {}).get('distance', float('inf'))) # ordena as atrações com base na proximidade
    
    with open('attractions.csv', 'w', newline='') as file: # escreve no ficheiro attractions.csv, em que newline='' é usado para evitar linhas em branco entre cada linha
        writer = csv.writer(file) # cria um objeto writer para escrever no ficheiro
        writer.writerow(["Tipo de Atração","Nome", "País", "Endereço", "Contacto", "Latitude", "Longitude", "Distância", "Fuso Horário", "Moeda"]) # escreve a primeira linha do ficheiro, que contém os nomes das colunas
        
        for attraction in attractions: # para cada atração na lista de atrações

            properties = attraction.get('properties', {}) # obtem as propriedades da atração
            distance = properties.get('distance', 'N/A') # se a chave 'distance' existir, atribui o seu valor à variável 'distance'. se não existir, atribui 'N/A'.

            if distance != 'N/A' and float(distance) <= maxDistance * 1000: # se a distância for diferente de 'N/A' e menor ou igual à distância máxima
                
                geometry = attraction.get('geometry', {}) # obtem a geometria da atração

                name = properties.get('name', 'N/A') # se a chave 'name' existir, atribui o seu valor à variável 'name'. se não existir, atribui 'N/A'.

                if name != 'N/A': # se o nome da atração for diferente de 'N/A'
                    attractionType = properties.get('categories', 'N/A')  # se a chave 'categories' existir, atribui o seu valor à variável 'attractionType'. se não existir, atribui 'N/A'.
                    country = properties.get('country', 'N/A') # se a chave 'country' existir, atribui o seu valor à variável 'country'. se não existir, atribui 'N/A'.
                    address = properties.get('formatted', 'N/A') # se a chave 'formatted' existir, atribui o seu valor à variável 'address'. se não existir, atribui 'N/A'.
                    contact = properties.get('contact', 'N/A') # se a chave 'contact' existir, atribui o seu valor à variável 'contact'. se não existir, atribui 'N/A'.
                    coordinates = geometry.get('coordinates', [0, 0]) # se a chave 'coordinates' existir, atribui o seu valor à variável 'coordinates'. se não existir, atribui as coordenadas [0, 0].
                    latitude, longitude = coordinates if len(coordinates) == 2 else (0, 0) # se houver 2 coordenadas, atribui-as às variáveis 'latitude' e 'longitude'. se não houver, atribui 0 e 0.
                    timezone = getTimezone(latitude, longitude) # chama a função getTimezone(), para obter o fuso horário da atração.
                    currency = getCurrency(country) # chama a função getCurrency(), para obter a moeda do país da atração.

                    writer.writerow([attractionType, name, country, address, contact, latitude, longitude, distance/1000, timezone, currency])
                    # escreve no ficheiro as informações obtidas da API, separadas por vírgula, numa linha


# Parte 5. Mostrar estatísticas básicas:


# função que devolve o nº de atrações, a distância média e as 3 atrações mais próximas
def showStatistics(attractions, maxDistance, count):
    numAttractions = count # calcula o nº de atrações
    distances = [attraction.get('properties', {}).get('distance', 0) for attraction in attractions] # para cada atração na lista de atrações
    # gera uma lista de distâncias para cada atração.
    # se a chave 'properties' existir, ela tenta obter a chave 'distance' dentro de 'properties'.
    # se qualquer chave não existir, o valor padrão 0 é atribuído à variável 'distances'

    # filtra as distâncias válidas (diferentes de 0 (valor padrão))
    validDistances = [dist for dist in distances if dist != 0 and dist <= maxDistance * 1000]

    if validDistances: # se houver distâncias válidas
        midDist = sum(validDistances) / len(validDistances) # calcula a distância média
    else: # se não houver distâncias válidas
        midDist = 0 # atribui 0 à distância média

    print(f"Número total de atrações: {numAttractions}")
    print(f"Distância média: {midDist/1000} km")

    # ordena as atrações com base na proximidade
    attractions.sort(key=lambda x: x.get('properties', {}).get('distance', float('inf')))
    # .sort() é usada para ordenar
    # a chave de ordenação é uma função lambda que extrai a distância de cada atração.
    # se uma atração não tiver uma distância definida, é atribuído o valor float('inf') para garantir que apareça no final da lista.

    '''
    float('inf') é uma representação do infinito positivo, ou seja, é um valor maior do que qualquer número real
    '''

    if numAttractions > 3: # se houver mais de 3 atrações
        print(f"\nTop 3 atrações mais próximas: ")

        validAttractions = [attraction for attraction in attractions if attraction.get('properties', {}).get('name', 'N/A') != 'N/A']
        # filtra as atrações válidas (com nome diferente de 'N/A'), criando uma nova lista

        for i, attraction in enumerate(validAttractions[:3]): # itera sobre as 3 atrações mais próximas, usando enumerate para obter tanto o índice (i) quanto a atração em cada iteração
            name = attraction.get('properties', {}).get('name', 'N/A')
            # tenta obter o nome da atração, se não existir, atribui 'N/A'.
            distance = attraction.get('properties', {}).get('distance', 'N/A')
            # tenta obter a distância da atração, se não existir, atribui 'N/A'.
            print(f"{i+1}. Nome: {name}, Distância: {distance/1000} km")
            # mostra a posição, o nome e a distância da atração


# Parte 6. Executar o programa principal:


# função main
def main():
    try: # tenta executar o código abaixo
        print("\nBEM-VINDO AO AJUDANTE DE PLANEAMENTO DE VIAGENS!\n\n")
        categories = readCategories() # chama função que lê o ficheiro categories.txt e armazena as categorias numa lista
        latitude, longitude, maxDistance, typesAttraction = getInformation() # chama a função que obtém informações, como a latitude, longitude, distância máxima e tipos de atrações, do utilizador
        attractions = getAttractions(latitude, longitude, maxDistance, typesAttraction) # chama a função que obtem as atrações disponíveis, com base na latitude, longitude, distância máxima e tipos de atrações dados pelo utilizador
        
        if attractions is not None:  # verifica se há atrações disponíveis
            count = showAttractions(attractions, maxDistance)  # chama a função que mostra as informações obtidas das APIs, consoante o pedido
            exportToCSV(attractions, maxDistance) # chama a função que guarda as informações obtidas das APIs num ficheiro CSV
            showStatistics(attractions, maxDistance, count)  # chama a função que devolve o nº de atrações, a distância média e as 3 atrações mais próximas
            print("\n\nTENHA UMA BOA VIAGEM!")
        else: # se não houver atrações disponíveis
            print("Não foi possível obter informações sobre atrações. Verifique os parâmetros fornecidos.")
    except Exception as e: # se houver um erro inesperado
        print(f"Erro inesperado: {e}")

# função para perguntar se o utilizador pretende ver outras atrações
def useAgain():
    try: # tenta executar o código abaixo
        while True:
            main() # chama, uma primeira vez, todo o código
            time.sleep(2) # espera 2 segundos
            answer = input('\nDeseja ver outras atrações? (s/n) ').lower()
            if answer == 's':
                os.system('clear') # limpa a consola (LINUX)
                '''Descomentar esta linha e comentar a linha anterior, caso esteja a usar Windows'''
                # os.system('cls') # limpa a consola (WINDOWS)
                continue # se sim, todo o código é executado de novo
            elif answer =='n': # caso contrário
                break # o código pára
            else: # se a resposta não for 's' ou 'n'
                print('Resposta Inválida!')
    except Exception as e: # se houver um erro inesperado
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    useAgain() # chama a função useAgain()