"""
Deve fazê-lo através da função _recursiva_ auxiliar `reverseAux`.
Eis um exemplo do cálculo:

    reverseAux(1234, 0)
    = reverseAux(123, 4)
    = reverseAux(12, 43)
    = reverseAux(1, 432)
    = reverseAux(0, 4321)
    = 4321

Não pode usar strings nem ciclos.
Note que `1234%10 = 4` e `1234//10 = 123`.
"""

def reverseDigits(value):
   return reverseAux(value, 0)

def reverseAux(partValue, partReversed):
   
    # quando a parte do valor original é 0, retornamos a parte invertida
    if partValue == 0:
        return partReversed
    
    # pega o último dígito da parte do valor original
    lastDigit = partValue % 10
    
    # atualiza a parte invertida, multiplicando por 10 e adicionando o último dígito
    updatedPartReversed = partReversed * 10 + lastDigit
    
    # chama recursivamente a função com os novos valores
    return reverseAux(partValue // 10, updatedPartReversed)