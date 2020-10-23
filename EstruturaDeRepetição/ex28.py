qtdCds=int(input('Informe a quantidade de Cds comprados: '))
cont=total=valorMedio=0
while cont < qtdCds:
    valor=float(input(f'Informe o valor do {cont+1}º CD: '))
    total+=valor
    cont+=1
valorMedio=total/qtdCds
print(f'Total investido em CDs: {total:.2f} R$')
print(f'Valor médio dos CDs: {valorMedio:.2f} R$')