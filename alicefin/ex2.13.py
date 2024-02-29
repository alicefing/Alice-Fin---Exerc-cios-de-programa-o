idade = int (input("Digite sua idade: "))
gênero = input ("Digite seu gênero (mulher ou homem): ")

if (gênero == "mulher" and idade >=60) or (gênero == "homem" and idade >= 65): 
    print ("Elegível para aposentadoria")
else:
    print ("Não elegível para aposentadoria")      