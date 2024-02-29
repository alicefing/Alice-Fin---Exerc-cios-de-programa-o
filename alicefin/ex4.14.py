frase = input("Digite uma frase: ")
palavras = frase.split()

for palavra in palavras:
    posicao = frase.find(palavra)
    print (f'A palavra {palavra} começa na posição {posicao}')
