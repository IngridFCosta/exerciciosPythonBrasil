"""8-Faça um programa que pergunte o preço de três produtos e informe qual
 produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
preço1=float(input('Escreva o preço do primeiro produto: '))
preço2=float(input('Escreva o preço do segundo produto: '))
preço3=float(input('Escreva o preço do terceiro produto: '))

menorPreço=preço1
if preço2< preço1 and preço2< preço3:
    menorPreço=preço2
    print('Você deve comprar o segundo produto pois é o mais barato')
if preço3< preço1 and preço3<preço2:
    menorPreço=preço3
    print('Você deve comprar o terceiro produto pois é o mais barato')
else:
    print('Você deve comprar o primeiro produto pois é o mais barato')

