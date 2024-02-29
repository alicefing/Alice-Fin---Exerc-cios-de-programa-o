numero_complexo_1_real = float(input("Digite a parte real de um número complexo: "))
numero_complexo_1_imaginaria = float(input("Digite a parte imaginária de um número complexo: "))
numero_complexo_2_real = float(input("Digite a parte real de outro número complexo: "))
numero_complexo_2_imaginaria = float(input("Digite a parte imaginária de outro número complexo: "))

soma_parte_real = numero_complexo_1_real + numero_complexo_2_real
soma_parte_imaginária = numero_complexo_1_imaginaria + numero_complexo_2_imaginaria

produto_parte_real = numero_complexo_1_real * numero_complexo_2_real - numero_complexo_1_imaginaria * numero_complexo_2_imaginaria
produto_parte_imaginária = numero_complexo_1_real * numero_complexo_2_imaginaria + numero_complexo_1_imaginaria * numero_complexo_2_real

print (soma_parte_real, "+", soma_parte_imaginária, "i", " --> É a soma dos números complexos")
print (produto_parte_real, "+", produto_parte_imaginária, "i", " --> É o produto dos números complexos")
