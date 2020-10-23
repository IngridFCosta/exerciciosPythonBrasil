listaNotas=[]
nomeAtleta=str(input('Informe o nome do atleta: '))
for cont in range(1,8):
    nota=float(input(f'Nota {cont}'))
    listaNotas.append(nota)

soma=sum(listaNotas)-max(listaNotas)-min(listaNotas)
print('RESULTADO FINAL:')
print(f'Atleta: {nomeAtleta}')
print(f'Melhor nota: {max(listaNotas)}')
print(f'Pior nota: {min(listaNotas)}')
print(f'Média: {soma/5:.2f}')