notas=[]
for x in range(1,5):
    notaAluno=float(input(f'Informe a {x}ª nota: '))
    notas.append(notaAluno)
print(f'Lista das notas: {notas}')
media=sum(notas)/4
print(f'A média das notas é: {media:.1f}')