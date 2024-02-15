# Given a string s and a string t, return a string in which all the characters 
# of s that occur in t have been replaced by a _ sign. The comparisons are 
# case sensitive.

def replaceCharactersWithUnderscores(s, t):
   
   result = ''
   
   for a in s: # para cada letra em s
      if a in t: # se essa letra existir em t
         result += '_'
      else: # se não existir em t
         result += a
            
   return result