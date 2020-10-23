soma=0
media=0
for x in range(1,6):
    numero=int(input(f'Informe o {x}º numero: '))
    soma+=numero
print(f'A soma é {soma}')
print(f'A media é {soma/5}')