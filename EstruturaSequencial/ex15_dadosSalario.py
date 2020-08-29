"""15-Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""
valorHora=float(input('Escreva quanto ganha por hora: '))
numHoras=int(input('Escreva o numero de horas trabalhadas: '))

salarioBruto=valorHora*numHoras
inss=(salarioBruto*8)/100
impostoR=(salarioBruto*11)/100
sindicato=(salarioBruto*5)/100
salarioLiquido=salarioBruto-inss-impostoR-sindicato
print('-'*8, 'Extrato do salário','-'*8)

print(f'Sálario bruto R$........... {salarioBruto:.2f}')
print(f'Desconto INSS R$........... {inss:.2f}')
print(f'Desconto sindicato R$.......{sindicato:.2f}')
print(f'Salário liquido R$......... {salarioLiquido:.2f}')
