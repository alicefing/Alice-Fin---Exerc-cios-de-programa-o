frase = input ("Digite uma frase: ")

for i in range (0, len(frase), 6):
    palavras = frase.split()
    print(frase[i:i+6])