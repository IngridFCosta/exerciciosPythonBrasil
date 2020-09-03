"""4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra=str(input('Escreva uma letra:'))
if letra in 'aeiou':
    print('A letra digitada é vogal')
else:
    print('A letra digitada é consoante')