distancia_percorrida = float(input("Digite a distância percorrida pelo objeto em metros: "))
tempo_gasto = float(input("Digite o tempo gasto em segundos: "))
aceleracao = float(input("Digite a aceleração do objeto em m/s²: "))

velocidade_inicial = (distancia_percorrida - 0.5 * aceleracao * tempo_gasto ** 2) / tempo_gasto 
velocidade_final = velocidade_inicial + aceleracao * tempo_gasto

print(f"A velocidade inicial é de {velocidade_inicial} m/s e a velocidade final é {velocidade_final} m/s")