"""11-Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a)o produto do dobro do primeiro com metade do segundo .
b)a soma do triplo do primeiro com o terceiro.
c)o terceiro elevado ao cubo."""

num1=int(input('Escreva um numero inteiro: '))
num2=int(input('Escreva outro numero inteiro: '))
num3=float(input('Escreva um numero real: '))
a=(num1*2)*(num2/2)
b=(num1*3)+num3
c=num3*num3*num3

print(f'produto do dobro do primeiro com metade do segundo: {a}')
print(f'a soma do triplo do primeiro com o terceiro: {b}')
print(f'terceiro elevado ao cubo: {c}')

