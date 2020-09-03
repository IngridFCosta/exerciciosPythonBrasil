"""6-Faça um Programa que leia três números e mostre o maior deles."""

primeiro=int(input('Escreva o primeiro número:'))
segundo=int(input('Escreva o segundo número:'))
terceiro=int(input('Escreva o terceiro número:'))

maior=primeiro
if segundo> primeiro and segundo>terceiro:
    maior=segundo
if terceiro > primeiro and terceiro >segundo:
    maior=terceiro
print('O maior valor digitado foi:{} '.format(maior))
