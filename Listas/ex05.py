valores=[]
valPares=[]
valImpares=[]

for x in range(1,21):
    numero=int(input(f'Informe o {x}º numero: '))
    valores.append(numero)
    if numero%2==0:
        valPares.append(numero)
    else:
        valImpares.append(numero)
print(f'Lista de valores: {valores}')
print(f'Lista de valores pares: {valPares}')
print(f'Lista de valores impares: {valImpares}')
