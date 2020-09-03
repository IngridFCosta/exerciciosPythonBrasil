"""21-Faça um Programa para um caixa eletrônico.O programa deverá perguntar
ao usuário a valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se
preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
 uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1."""

print('='*30)
print('{:^30}'.format('Caixa Eletrônico'))
print('='*30)
valor=int(input('Que valor você quer sacar? R$ '))
total=valor
ced=100
totalCed=0
while True:
    if total>=ced:
        total-=ced
        totalCed+=1
    else:
        if totalCed>0:
            print(f'Total de {totalCed} cedulas de R${ced} reais')
        if ced==100:
            ced=50
        elif ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=5
        elif ced==5:
            ced=1
        totalCed=0
        if total==0:
            break