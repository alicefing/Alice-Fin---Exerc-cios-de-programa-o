numero = [1, 2, 3, 4, 5, 6]

numero[1::2] = numero[1::2][::-1]
print (f"{numero} --> lista de números pares invertidos")