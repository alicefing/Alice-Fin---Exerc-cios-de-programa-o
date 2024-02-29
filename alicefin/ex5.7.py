alunos_notas = {}
numero_alunos = int (input("Digite a quantidade de alunos que deseja inserir: "))

for i in range(numero_alunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos_notas[nome] = nota

alunos_notas_finais = {nome: round(nota) for nome, nota in alunos_notas.items()}

print("Dicionário com notas as notas finais:")
print(alunos_notas_finais)