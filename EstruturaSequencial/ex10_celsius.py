"""10-Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit."""

from time import sleep
grausC=float(input('Escreva a  temperatura em graus Celsius: '))
fahrenheit=(grausC*9/5)+32
print('Convertendo...')
sleep(1)
print(f'A temperatura em graus Fahrenheit é: {fahrenheit:.0f}°')