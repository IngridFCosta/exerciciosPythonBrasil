"""8-Faça um Programa que peça a temperatura em graus Fahrenheit,
 transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)."""
from time import sleep
grausF=float(input('Escreva a  temperatura em graus Fahrenheit: '))
celsius=5*((grausF-32)/9)
print('Convertendo...')
sleep(1)
print(f'A temperatura em graus Celsius é: {celsius:.2f}°')