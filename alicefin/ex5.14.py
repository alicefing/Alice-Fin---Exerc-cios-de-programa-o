notas_alunos = [10, 20, 30, 40]
nomes_alunos = ["Alice", "Isa", "Yasmin", "Maria"]

alunos_notas = list (zip(nomes_alunos, notas_alunos))
alunos_notas_decresente = sorted(alunos_notas, key=lambda x: x[1], reverse=True)

print ("Ordem decrescente:")
for aluno, nota in alunos_notas_decresente:
    print(aluno, "-->", nota)