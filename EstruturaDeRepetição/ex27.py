qtdTurmas=int(input('Informe a quantidade de turmas: '))
mediaAlunos=cont=soma=0

while cont < qtdTurmas:
    totAluno=int(input(f'Informe o total de alunos da {cont+1}ª turma: '))
    if totAluno >40:
        print('Turma Lotada!')
        totAluno=int(input(f'Informe o total de alunos da {cont+1}ª turma: '))
    cont+=1
    soma+=totAluno
mediaAlunos=soma/qtdTurmas
print(f'A media de alunos por turma é: {mediaAlunos:.0f}')