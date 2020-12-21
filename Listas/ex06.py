listaNotas=[]
media=[]
totAlunosMaior=0
for x in range(1,3):
    notas=[]
    print(f'Notas {x}º aluno')
    for x in range(1,5):
        notas.append(float(input(f'Escreva a {x}ª nota: ')))
        mediaNotas=sum(notas)/len(notas)
    listaNotas.append(notas)
    if mediaNotas >=7.0:
        media.append(mediaNotas)
print(f'Lista de notas: {listaNotas}')
print(f'Total de alunos com média maior ou igua a 7.0: {len(media)}')
