"""23-Faça um Programa que peça um número e informe se o
 número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""
numero=float(input('Escreva um número: '))

if numero==round(numero):
    print(f'O numero {numero:.0f} é inteiro')
else:
    print(f'O numero {numero} é decimal')