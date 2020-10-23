respostaProf = []
totNotas = []
respostasAluno=[]
print('-'*10,'Professor','-'*10)
for cont in range(10):
    gabarito=respostaProf.append(input(f'Digite a resposta da {cont+1}ª questão:'))

print('-'*10,'Respostas do Aluno','-'*10)
continuar = True
while continuar != 'N':
    respostasAluno.clear()
    for cont in range(10):
        resposta = respostasAluno.append(input(f'Digite a resposta da {cont+1}ª questão:'))
    nota = 0
    for cont in range(10):
        if respostasAluno[cont] == respostaProf[cont]:
            nota += 1
    totNotas.append(nota)
    continuar = input("Outro aluno vai utilizar o sistema? [s/n] : ").upper().strip()

print(f'Total de alunos que utilizaram o sistema: {len(totNotas)}')
print(f'Maior nota: {max(totNotas)}')
print(f'A menor nota:{min(totNotas)}')
print(f'A media de notas da turma foi: {sum(totNotas) / len(totNotas)}')
