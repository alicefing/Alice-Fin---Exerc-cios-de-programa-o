frase = input("Digite uma frase: ")
palavras = frase.split()

frase_sem_espaco = [palavra.strip() for palavra in palavras]
frase_nova = ' '.join(frase_sem_espaco)

print("Frase sem espaços:", frase_nova)