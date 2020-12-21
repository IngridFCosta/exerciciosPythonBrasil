numeros=[]
mult=1
for x in range(1,6):
    numeros.append(int(input(f'Informe o {x}º número: ')))
for cont in numeros:
    mult*=cont
print(f'Lista dos números: {numeros}')
print(f'Soma dos números: {sum(numeros)}')
print(f'Multiplicação: {mult}')

