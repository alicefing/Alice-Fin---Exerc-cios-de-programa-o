numero = int (input ("Digite um número: "))

while True:
   if numero < 0:
    break
   print("Você digitou o número", numero)
   numero = int(input("Digite outro número: "))
print("Você digitou um número negativo.")