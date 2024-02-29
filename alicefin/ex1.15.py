import math

distancia = float (input ("Digite a distância em metros: "))
velocidade_inicial = float (input("Digite a velocidade inicial (m/s): "))
gravidade = 9.8

tempo = math.sqrt ((2*distancia) / gravidade)

print (f"O tempo do queda livre é de: {tempo} segundos" )
