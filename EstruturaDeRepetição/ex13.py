base=int(input('Informe a base: '))
expoente=int(input('Informe o expoente: '))

cont=1
resultado=1
while cont <= expoente:
    resultado*=base
    cont+=1
print(f'{base}^{expoente}={resultado}')