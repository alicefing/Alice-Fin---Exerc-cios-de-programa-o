import math

numeroA = int(input("Digite um número para a: "))
numeroB = int (input("Digite um número para b: "))
numeroC = int (input("Digite um número para c: "))

delta = numeroB ** 2 - (4 * numeroA * numeroC)

if delta == 0:
   print ("O valor de A tem que ser diferente de 0")
elif delta < 0:
    print ("Sem raízes reais")  
else:
    x1 = (-numeroB + math.sqrt (delta)) / (numeroA * 2)
    x2 = (-numeroB - math.sqrt (delta)) / (numeroA * 2)
    print (f"A raíz 1 é: {x1}")
    print (f"A raíz 2 é: {x2}")