"""12-Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do
salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que
o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário
Bruto menos os descontos. O programa deverá pedir ao usuário o valor
da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

valorHora=float(input('Escreva o valor da hora em reais: '))
qtdHoras=int(input('Escreva a quantidade de horas trabalhadas no mês: '))
salBruto=valorHora*qtdHoras

if salBruto <=900.00:
    inss=(salBruto*10)/100
    salLiquido=salBruto-inss
    fgts=(salBruto*11)/100
    print(f'Salario Bruto: ({valorHora}* {qtdHoras}):{salBruto: >32}')
    print(f'(-) IR:............................................... Isento')
    print(f'((-)INSS (10%):    {inss: >40}')
    print(f'FGTS (11%):        {fgts: >40}')
    print(f'Total de descontos:{inss: >40}')
    print(f'Salário liquido:   {salLiquido: >40}')

elif salBruto > 900.00 and salBruto <=1500.00:
    inss=(salBruto*10)/100
    impRenda=(salBruto*5)/100
    fgts=(salBruto*11)/100
    salLiquido=salBruto-inss-impRenda
    print(f'Salario Bruto: ({valorHora}* {qtdHoras}):{salBruto: >32}')
    print(f'(-) IR :           {impRenda: >40}')
    print(f'((-)INSS (10%):    {inss: >40}')
    print(f'FGTS (11%):        {fgts: >30}')
    print(f'Total de descontos:{inss+impRenda: >40}')
    print(f'Salário liquido:   {salLiquido: >40}')

elif salBruto > 1500.00 and salBruto <=2500.00:
    inss=(salBruto*10)/100
    impRenda=(salBruto*10)/100
    fgts=(salBruto*11)/100
    salLiquido=salBruto-inss-impRenda
    print(f'Salario Bruto: ({valorHora} *{qtdHoras}):{salBruto: >30s}')
    print(f'(-) IR:             {impRenda: >40}')
    print(f'((-)INSS (10%):    {inss: >40}')
    print(f'FGTS (11%):        {fgts: >40}')
    print(f'Total de descontos:{inss+impRenda: >40}')
    print(f'Salário liquido:   {salLiquido: >40}')
elif salBruto > 2500.00:
    inss=(salBruto*10)/100
    impRenda=(salBruto*20)/100
    fgts=(salBruto*11)/100
    salLiquido=salBruto-inss-impRenda
    print(f'Salario Bruto: ({valorHora}* {qtdHoras}):{salBruto: >33}')
    print(f'(-) IR:            {impRenda: >40}')
    print(f'((-)INSS (10%):    {inss: >40}')
    print(f'FGTS (11%):        {fgts: >40}')
    print(f'Total de descontos:{inss+impRenda: >40}')
    print(f'Salário liquido:   {salLiquido: >40}')

