import re

nome_usuário = input("Digite seu nome: ")
senha = str (input("Digite sua senha com caracteres alfanúmericos : "))

texto_sem_especiais = re.sub('[^A-Za-z0-9]+', ' ', senha)
print(f'{texto_sem_especiais}é a senha sem os caracteres alfanuméricos')