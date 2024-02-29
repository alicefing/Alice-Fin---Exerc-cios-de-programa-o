frase = input ("Digite uma frase: ")

palavras = frase.split()
artigos = ['o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas']

frase_nova = frase
for artigo in artigos:
    frase_nova = frase_nova.replace(artigo, "")

print("Frase sem artigos:", frase_nova)