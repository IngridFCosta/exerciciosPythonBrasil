termos=int(input('Quantos termos deseja mostrar? '))
cont=termos-1
numero1=1
numero2=1
soma01=soma02=0
print(f'S= {numero1}/{numero1} + ', end=' ')
while cont > 0:
    numero1+=1
    numero2+=2
    print(f'{numero1}/{numero2}', end=' ')
    soma01+=numero1
    soma02+=numero2
    print(' + ' if cont > 1 else '=', end='')
    cont-=1
print(soma01+1,'/', soma02+1)
