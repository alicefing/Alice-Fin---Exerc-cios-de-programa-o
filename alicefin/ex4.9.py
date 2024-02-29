frase = input("Digite uma frase: ")
palavra_presente = input("Digite uma palavra presente na frase: ")
palavra_ausente = input("Digite uma palavra ausente na frase: ")

frase_nova = frase.replace(palavra_presente, palavra_ausente)
print("Frase modificada:", frase_nova)