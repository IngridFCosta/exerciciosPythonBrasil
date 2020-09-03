"""24-Faça um Programa que leia 2 números e em seguida pergunte
ao usuário qual operação ele deseja realizar. O resultado da operação
deve ser acompanhado de uma frase que diga se o número é: par ou ímpar;
positivo ou negativo;
inteiro ou decimal."""

num1=float(input('Escreva o primeiro número: '))
num2=float(input('Escreva o segundo número: '))
print('+ adição\n'
      '- Subtração\n'
      '* Multiplicação\n'
      '/ Divisão')

operacao=str(input('Qual operação deseja realizar? '))
if operacao=='+':
    resultado=num1+num2
    if resultado %2==0:
        print('O numero é par')
    else:
        print('O numero é impar')
    if resultado > 0:
        print('O numero é positivo')
    else:
        print('O numero é negativo')
    if resultado==round(resultado):
        print('O numero é inteiro')
    else:
        print('O numero é decimal')
elif operacao=='-':
    resultado=num1-num2
    if resultado %2==0:
        print('O numero é par')
    else:
        print('O numero é impar')
    if resultado > 0:
        print('O numero é positivo')
    else:
        print('O numero é negativo')
    if resultado==round(resultado):
        print('O numero é inteiro')
    else:
        print('O numero é decimal')
elif operacao=='*':
    resultado=num1*num2
    if resultado %2==0:
        print('O numero é par')
    else:
        print('O numero é impar')
    if resultado > 0:
        print('O numero é positivo')
    else:
        print('O numero é negativo')
    if resultado==round(resultado):
        print('O numero é inteiro')
    else:
        print('O numero é decimal')
elif operacao=='/':
    resultado=num1/num2
    if resultado %2==0:
        print('O numero é par')
    else:
        print('O numero é impar')
    if resultado > 0:
        print('O numero é positivo')
    else:
        print('O numero é negativo')
    if resultado==round(resultado):
        print('O numero é inteiro')
    else:
        print('O numero é decimal')

