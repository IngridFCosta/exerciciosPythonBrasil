"""9-Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
num1=int(input('Escreva o primeiro número:'))
num2=int(input('Escreva o segundo número: '))
num3=int(input('Escreva o terceiro número: '))

lista = [num1, num2, num3]

lista.sort(key=float, reverse=True)

print("decrescente: ", lista)
