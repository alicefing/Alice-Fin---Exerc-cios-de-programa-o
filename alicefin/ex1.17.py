preço_mercadoria = int (input ("Digite o preço da mercadoria (em R$): "))
desconto = int (input("Digite o desconto da mercadora (em R$): "))
imposto = int (input("Digite o imposto da mercadora (em R$): "))

preco_descontado = preço_mercadoria * (1 - desconto / 100)
preco_final = preco_descontado * (1 + imposto / 100)

print (f"O preço final da mercadoria é de {preco_final} reais")