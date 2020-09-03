"""7-Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
primeiro=int(input('Escreva o primeiro número:'))
segundo=int(input('Escreva o segundo número:'))
terceiro=int(input('Escreva o terceiro número:'))

maior=primeiro
if segundo > primeiro and segundo > terceiro:
    maior=segundo
if terceiro > primeiro and terceiro >  segundo:
    maior=terceiro

menor=primeiro
if segundo< primeiro and segundo< terceiro:
    menor=segundo
if terceiro< primeiro and terceiro< segundo:
    menor=terceiro

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')