vogais = "aeiou"
consoantes = "bcdfghjqlmnpqrstvwxyz"

letra = input ("Digite uma letra: ")

if len (letra) ==1:
   if letra in vogais:
    print ("Isso é uma vogal")
   elif letra in consoantes:
    print ("Isso é uma consoante")    
   else:
    print ("Você não digitou uma letra")     
else:
   print ("Você digitou mais de um caractere")    