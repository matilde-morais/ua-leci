# Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
   
   prefixo = ""
   preMax = ""
   
   for i in range(len(s)):
      prefixo += s[i]
      if prefixo in s[i+1:]:
         preMax = prefixo
         
   return preMax