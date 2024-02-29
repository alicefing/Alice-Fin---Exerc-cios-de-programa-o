numeros = []

for i in range(10):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

    
maior_numero = max(numeros)
menor_numero = min (numeros)

print (f'O {maior_numero} é o maior número da lista')
print (f'O {menor_numero} é o menor número da lista')