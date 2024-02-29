frase = input("Digite uma frase: ")

palavras = frase.split()
ocorrencias_o = sum(palavra.lower().endswith("o") for palavra in palavras)
ocorrencias_a = sum(palavra.lower().endswith("a") for palavra in palavras)

print("O número de palavras que terminam com 'o' é:", ocorrencias_o)
print("O número de palavras que terminam com 'a' é:", ocorrencias_a)