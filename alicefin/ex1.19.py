velocidade_inicial = int (input("Digite a velocidade inicial (m/s):"))
velocidade_final = int (input("Digite a velocidade final (m/s): "))
tempo = int(input("Digite o tempo gasto em segundos: "))

aceleração = (velocidade_inicial - velocidade_final) / tempo
print (f'A aceleração desse objeto é de {aceleração} m/s²')
