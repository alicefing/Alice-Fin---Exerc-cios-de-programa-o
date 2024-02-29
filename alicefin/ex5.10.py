palavras = (input("Digite uma lista de palavras separados por espaços:")) .split ()
palavras_comprimento = list (map(lambda palavras: len (palavras), palavras))
print(palavras_comprimento) 
 