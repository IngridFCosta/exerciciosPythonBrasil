numero=int(input('Informe um número para calcular o fatorial: '))
fatorial=1
contador=numero
while contador > 0:
    print(contador, end='')
    fatorial*=contador
    print(' x ' if contador > 1 else ' = ',end='')
    contador-=1
print(fatorial)