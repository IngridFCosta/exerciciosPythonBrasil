nota=True
notas=[]
acimaMedia=[]
abaixoSete=[]
while nota !=-1:
    nota=float(input('Escreva uma nota: '))
    if nota==-1:
        break
    else:
        notas.append(nota)
#A
print(f'Quantidade de notas lidas: {len(notas)}')
#B
print('Notas-> ', end='')
for x in notas:
    print(f'{x}', end=' ')
#C
print()
print('Notas na ordem inversa->', end=' ')
notas.reverse()
for x in notas:
    print(f'{x}', end=' ')
print()
#D
print(f'Soma das notas: {sum(notas)}')
#E
media=sum(notas)/ len(notas)
print(f'Média das notas: {media:.2f}')
#F
for x in range (len(notas)):
    if notas[x] > media:
        acimaMedia.append(notas[x])
    elif notas[x] < 7:
        abaixoSete.append(notas[x])
print(f'Quantidade de valores acima da média: {len(acimaMedia)}')
#G
print(f'Quantidade de valores abaixo de sete: {len(abaixoSete)}')
#H
print('Programa encerrado!!!')