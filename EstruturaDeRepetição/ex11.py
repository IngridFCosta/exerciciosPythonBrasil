
num1=int(input('Informe o primeiro numero: '))
num2=int(input('Informe o segundo numero: '))
soma=0
print(f'Numeros no  intervalo de {num1} e {num2}')
for x in range(num1+1, num2):
    print(x, end=' ')
    soma+=x
print()
print(f'A soma é {soma}')