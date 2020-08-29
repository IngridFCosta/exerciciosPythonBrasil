"""12-Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
from time import sleep
altura=float(input('Escreva sua altura: '))
pesoIdeal=(72.7*altura)-58
print('Calculando...')
sleep(1)
print(f'O peso ideal será de: {pesoIdeal:.2f}')