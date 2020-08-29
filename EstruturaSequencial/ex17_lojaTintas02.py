"""17- Faça um Programa para uma loja de tintas. O programa deverá
pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6
metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
-comprar apenas latas de 18 litros;
-comprar apenas galões de 3,6 litros;
-misturar latas e galões, de forma que o desperdício de tinta seja menor.
 Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

from math import ceil

areaTotal=float(input('Escreva a area a ser pintada em M²: '))
qtdTinta=areaTotal/6
totLatas2=qtdTinta/3.6
totLatas=int(qtdTinta/18)

sobraTinta=qtdTinta%18

resto= sobraTinta/3.6

preçoTotal=80*ceil(totLatas)
preçoTotal2=25*(ceil(totLatas2))
precoMistura=80*ceil(totLatas)+25*(ceil(totLatas2))

print(f'A quantidade de latas de 18 litros é : {ceil(totLatas)}')
print(f'Preço total com latas de 18 litros é: {preçoTotal:.2f}')

print(f'A quantidade de latas de 3.6 litros é : {ceil(totLatas2)}')
print(f'Preço total com latas de 3.6 litros é: {preçoTotal2:.2f}')

print(f'A quantidade de latas de 18 litros é: {ceil(totLatas)} e de 3.6 é de {ceil(resto)}')
print(f'Preço total com latas misturadas é: {precoMistura:.2f}')