alunos_notas = {}
numero_alunos = int (input("Digite a quantidade de alunos que deseja inserir: "))

for i in range(numero_alunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos_notas[nome] = nota


alunos_notas_finais = {nome: round(nota) for nome, nota in alunos_notas.items() if nota >= 7}

print(f"{alunos_notas_finais} --> nota igual ou maior que 7")
