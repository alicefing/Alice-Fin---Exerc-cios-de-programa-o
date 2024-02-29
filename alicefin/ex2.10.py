numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite um número: "))
numero3 = int(input("Digite um número: "))

soma = numero1 + numero2 + numero3
média = soma / 3

if média == 10:
    print ("Parabéns") 
elif média >= 6:
    print ("Aprovado") 
else:
    print ("Reprovado")       
