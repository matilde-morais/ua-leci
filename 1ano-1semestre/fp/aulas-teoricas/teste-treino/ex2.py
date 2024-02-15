# ID: 118866

"""
Imagine que está a fazer palavras cruzadas (em Inglês) e falta-lhe uma
palavra com o padrão "?YS???Y", onde os "?" representam letras por preencher.
Complete este programa para o ajudar a descobrir a palavra.
O programa já inclui instruções para ler uma lista de palavras inglesas a
partir do ficheiro wordlist.txt.
"""

# This function reads words from a file.
def load(fname):
   with open(fname) as f:
      lst = []
      for line in f:
         words = line.strip().split()
         lst.extend(words)
   return lst


""" a)
Complete a função matchesPattern(s, pattern) para devolver
True se s corresponder ao padrão fornecido e False, no caso contrário.
Uma string s corresponde ao padrão se e só se tiver os mesmos carateres
que o padrão nas mesmas posições, exceto onde o padrão tem ?.
Nas posições dos ?, não importa que carateres estão na string s.
A correspondência não deve fazer distinção entre maiúsculas e minúsculas.
"""
def matchesPattern(s, pattern, lst):
   letras = list(s.lower())
   
   for word in lst:
      letters = list(pattern.lower())
      if len(letters)==len(letras):
         match = True
         for i in range(len(letras)):
            if letters[i] != "?" and letras[i] != letters[i]:
               match = False
               break
            elif letters[i] != "?" and letras[i] == letters[i]:
               match = True
            else:
               match = False
               break
         if match:
            return True
   return False

""" b)
Complete a função filterPattern(lst, pattern) para extrair duma lista de strings
as strings que têm o padrão dado.
Sugestão: use a função matchesPattern para testar cada palavra.
"""
def filterPattern(lst, pattern):
   
   padroes = []
   
   for s in lst:
    if matchesPattern(s, pattern, lst):
      padroes.append(s)
   return padroes



def main():
   
   words = load("wordlist.txt")
   
   print("a)")
   print( matchesPattern("secret", "s?c??t", words) )  #-> True
   print( matchesPattern("secreta", "s?c??t", words) ) #-> False
   print( matchesPattern("socket", "s?c??t", words) )  #-> True
   print( matchesPattern("soccer", "s?c??t", words) )  #-> False
   print( matchesPattern("SEcrEt", "?ecr?t", words) )  #-> True
   print( matchesPattern("SEcrET", "?ecr?t", words) )  #-> True
   print( matchesPattern("SecrEt", "?ECR?T", words) )  #-> True

   print("b)")
   # Solution to "S?C??T"
   lst = filterPattern(words, "s?c??t")
   print(lst)

   assert isinstance(lst, list),  "result lst should be a list"
   assert "secret" in lst,  "result should contain 'secret'"

   # Solution to "?YS???Y"
   lst = filterPattern(words, "?ys???y")
   print(lst)


# Call main function:
if __name__ == "__main__":
   main()