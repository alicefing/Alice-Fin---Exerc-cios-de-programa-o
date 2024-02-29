frase = input("Digite uma frase: ")
palavras = frase.split()
numero_palavras = {}

for palavra in palavras:
    if palavra in numero_palavras:
        numero_palavras [palavra] +=1
    else:
        numero_palavras [palavra] = 1
print("Número de ocorrências de cada palavra:")

for palavra, contagem in numero_palavras.items():
    print(f"A palavra '{palavra}' aparece {contagem} vezes.")     