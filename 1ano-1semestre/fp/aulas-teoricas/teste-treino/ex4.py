'''O Método de Hondt permite fazer a distribuição de deputados eleitos para uma assembleia de forma proporcional aos votos de cada partido. Considerando que V_i é o número de votos obtidos pelo partido i, o método determina o número N_i de lugares a atribuir a esse partido.

O método começa com N_i = 0 para todos os partidos e depois:

Calcula os quocientes Q_i = \frac{V_i}{N_i+1}.
Encontra o partido com o maior quociente e atribui-lhe um deputado (aumenta o N_i correspondente).
Se vários partidos tiverem quocientes iguais, atribui o deputado ao partido com menos votos.
Repete estes passos até todos os lugares estarem atribuídos.
Por exemplo, para distribuir 6 lugares por quatro partidos que tiveram as votações V = [15300, 12000, 6600, 5100] o processo deve seguir os passos abaixo.

Q: [15300, 12000, 6600, 5100] => +1 for party 0 => N: [1, 0, 0, 0]
Q: [ 7650, 12000, 6600, 5100] => +1 for party 1 => N: [1, 1, 0, 0]
Q: [ 7650,  6000, 6600, 5100] => +1 for party 0 => N: [2, 1, 0, 0]
Q: [ 5100,  6000, 6600, 5100] => +1 for party 2 => N: [2, 1, 1, 0]
Q: [ 5100,  6000, 3300, 5100] => +1 for party 1 => N: [2, 2, 1, 0]
Q: [ 5100,  4000, 3300, 5100] => +1 for party 3 => N: [2, 2, 1, 1]
Note que o 1º deputado vai para o partido 0, porque tem o quociente mais alto. Depois atualiza-se Q e repete-se. No último passo há dois partidos com Q máximo, por isso atribui-se o lugar ao partido menos votado.

Implemente uma função hondt(votes, numseats) que, dada uma lista com os números de votos em cada um partidos e dado o número de lugares disponíveis, calcule e devolva uma lista com a distribuição de deputados para cada partido. Por exemplo, hondt([15300, 12000, 6600, 5100], 6) deve devolver [2, 2, 1, 1].

'''

def hondt(votes, numseats): # dão o nº de votos de todos os partidos e o nº de lugares a distribuir
   
   partidos = len(votes) # nº de partidos
   
   lugares = [0] * partidos # criar lista para o nº de lugares destinado a cada partido
   
   while numseats > 0: # até já não haver luagres disponíveis
      
      quociente = [votes[i]/(lugares[i]+1) for i in range(partidos)] # faz uma nova lista dos quocientes
      max_quociente_value = max(quociente) # encontra o maior valor dos quocientes
      max_quociente_index = quociente.index(max_quociente_value) # encontra o index do maior valor dos quocientes
      
      empate_indices = [i for i, q in enumerate(quociente) if q == max_quociente_value] # forma duplas de indices e quocientes. guarda uma lista de indices onde quocientes sejam iguais.

      if len(empate_indices) > 1:  # s houver empate, atribui ao partido menos votado
         menos_votado_index = min(empate_indices, key=lambda x: votes[x]) # encontra o indice do menos votado do empate
         lugares[menos_votado_index] += 1 # atribui um voto
      else:
         lugares[max_quociente_index] += 1 # se nao houver empate, atribui 1 voto ao partido com maior quociente
      
      numseats -= 1 # diminui-se o nº de lugares disponiveis
      
   return lugares
