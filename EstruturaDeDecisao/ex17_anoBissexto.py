"""17-Faça um Programa que peça um número
correspondente a um determinado ano e em seguida
informe se este ano é ou não bissexto."""

ano=int(input('Escreva um ano para verificar se é bissexto ou não: '))
if ano%4==0  and ano %100!=0 or ano%400==0:
    print('\033[0;32mO ano é bissexto!')
else:
    print('\033[0;34mO ano não é bissexto!')