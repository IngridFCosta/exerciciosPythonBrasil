totNum=int(input('Informe o total de numeros que você quer mostrar:  '))
soma=maior=menor=0
for x in range(0,totNum):
    numero=int(input(f'Informe o {x+1}º número: '))
    while numero < 0  or numero > 1000:
        print('Numero inválido!')
        numero=int(input(f'Informe o {x+1}º número: '))
    if x==0:
        maior=menor=numero
    if numero > maior:
        maior=numero
    elif numero < menor:
        menor=numero
    soma+=numero
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
print(f'A soma é {soma}')