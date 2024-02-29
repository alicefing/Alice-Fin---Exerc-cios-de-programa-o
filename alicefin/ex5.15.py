numeros = [12, 14, 16, 18, 20]
referencia = 15

posicao = next((i for i, num in enumerate(numeros) if num > referencia), len(numeros))
print (f"{posicao}° --> posição do primeiro elemento maior que a referência")