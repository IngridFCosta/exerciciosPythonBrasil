alunos13=[]
alturas=[]
for x  in range (1,31):
    idade=int(input(f'Informe a idade do {x}º aluno (a): '))
    altura=float(input(f'Informe a altura do {x}º aluno (a): '))
    alturas.append(altura)
    media=(sum(alturas))/len(alturas)

    if idade > 13 and altura < media:
        alunos13.append(idade)

print(alturas)
print(f'Média das alturas: {media:.2f}')
print(f'Total de alunos maiores de 13 anos e altura abaixo da média: {len(alunos13)}')

