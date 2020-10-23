"""Fatorial"""

numero=int(input('Escreva um numero para calcular o fatorial: '))
cont=numero
fatorial=1
while cont >0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial*=cont
    cont-=1
print(fatorial)
