valorDivida=float(input('Informe o valor da divida: '))
print(f'Valor da divida', end='      ')
print('Qtd Parcelas', end='      ')
print('Total de juros',end='      ')
print('Valor da parcela')
juro=0
for parcela in range(0,18,3):
    if parcela==0:
        parcela=1
        print(f'{valorDivida:.2f}', end='                ')
        print(parcela, end='                  ')
        print(juro,end='                  ')
        print(f'{valorDivida/parcela:.2f}')
    if parcela==3:
        juro=10
        totJuro=(valorDivida*10)/100
        valorTotal=totJuro+valorDivida
        print(f'{valorDivida+totJuro:.2f}', end='                ')
        print(parcela, end='                  ')
        print(f'{totJuro:.2f}',end='                  ')
        print(f'{valorDivida/parcela:.2f}')
    if parcela==6:
        juro=15
        totJuro=(valorDivida*15)/100
        valorTotal=totJuro+valorDivida
        print(f'{valorDivida+totJuro:.2f}', end='                ')
        print(parcela, end='                  ')
        print(f'{totJuro:.2f}',end='                  ')
        print(f'{valorDivida/parcela:.2f}')
    if parcela==9:
        juro=20
        totJuro=(valorDivida*20)/100
        valorTotal=totJuro+valorDivida
        print(f'{valorDivida+totJuro:.2f}', end='                ')
        print(parcela, end='                  ')
        print(f'{valorDivida/parcela:.2f}')
    if parcela==12:
        juro=25
        totJuro=(valorDivida*25)/100
        valorTotal=totJuro+valorDivida
        print(f'{valorDivida+totJuro:.2f}', end='                ')
        print(parcela, end='                 ')
        print(f'{totJuro:.2f}',end='                  ')
        print(f'{valorDivida/parcela:.2f}')




