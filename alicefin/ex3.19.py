texto = (input("Digite um texto: "))
texto_invertido = texto [::-1]

if texto_invertido == texto:
    print (f"A palavra {texto} é um palíndromo")
else:
    print(f"A palavra {texto} não é um palíndromo")    
