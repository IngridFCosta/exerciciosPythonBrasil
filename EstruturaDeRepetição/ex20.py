numero=int(input('Informe um número pra calcular o fatorial: '))
cont=numero
fatorial=1
if numero > 16:
    numero=int(input('Informe um número pra calcular o fatorial: '))
    while cont > 0:
        print(cont, end='')
        print(' x ' if cont > 1 else ' = ', end='')
        fatorial*=cont
        cont-=1
    print(fatorial)




