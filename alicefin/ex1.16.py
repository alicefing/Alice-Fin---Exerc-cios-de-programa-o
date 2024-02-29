valor_inicial_investimento = int (input("Digite um valor para o investimento inicial (R$): "))
taxa_juros = int (input("Digite um valor para a taxa de juros (R$): "))
n_anos = int (input ("Digite o número de anos: "))

taxa_juros_decimal = taxa_juros / 100
valor_final = valor_inicial_investimento * (1 + taxa_juros_decimal) ** n_anos

print("O valor final do investimento é:", valor_final)