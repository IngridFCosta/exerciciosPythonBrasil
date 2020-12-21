salarios=[]
menorAbono=0
pisoAbono=100
abono=0
totaAbono=[]
strCabecalho='Projeção de gastos com abono'
print(strCabecalho)
print('='*len(strCabecalho))
salario =True
while salario !=0:
    salario=float(input('Digite o valor do salário: '))
    if salario==0:
        break
    salarios.append(salario)
print()
print('Salários', end="               ")
print('Valor do abono')
for x in range(len(salarios)):
    if salarios[x] >=1000:
            abono=salarios[x]*0.2
    elif salarios[x] < 1000:
        abono=pisoAbono
        menorAbono+=1
    totaAbono.append(abono)
    print(f' R$ {salarios[x]:.2f} ------------------ R${abono:.2f}')

print(f'Foram processados {len(salarios)} colaboradores')
print(f'Total gasto com abonos: {sum(totaAbono):.2f}')
print(f'Valor minimo pago a {menorAbono} colaboradores')
print(f'Maior valor de abono pago foi de: {max(totaAbono):.2f} R$')




