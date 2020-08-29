"""6-Faça um Programa que peça o raio de um círculo, calcule e mostre sua área"""

from math import pi
raioCirculo=int(input('Escreva o raio do circulo: '))
area=pi* (raioCirculo*raioCirculo)

print(f'A area do circulo é: {area:.2f}')