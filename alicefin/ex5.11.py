numeros = (input("Digite uma lista de números separados por espaços:")) .split ()
numeros_pares = [int(num) for num in numeros if int(num) % 2 == 0]

print(f" {numeros_pares} são os números pares") 