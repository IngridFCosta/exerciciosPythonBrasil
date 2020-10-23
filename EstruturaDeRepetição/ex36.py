"""Tabuada com limite"""

tabNumero=int(input('Informe um número para calcular sua tabuada:'))
inicio=int(input('Começa por: '))
fim=int(input('Terminar em: '))
if fim > inicio:
    print(f'Vou fazer a tabuada do {tabNumero}, começando por {inicio} terminando em {fim}')
    for cont in range(inicio, fim+1):
        print(f'{tabNumero} x {cont}={tabNumero*cont}')
else:
    print('Erro! Você digitou um fim menor que o inicio')
