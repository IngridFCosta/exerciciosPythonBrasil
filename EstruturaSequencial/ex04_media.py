"""4-Faça um Programa que peça as 4 notas bimestrais e mostre a média."""

print('-'*10,'Notas Bimestrais','-'*10)
nota1=float(input('Escreva a nota do primeiro bimestre: '))
nota2=float(input('Escreva a nota do segundo bimestre: '))
nota3=float(input('Escreva a nota do terceiro bimestre: '))
nota4=float(input('Escreva a nota do quarto bimestre: '))

media=(nota1+nota2+nota3+nota4)/4
print(f'A média do alunos é {media:.2f}')