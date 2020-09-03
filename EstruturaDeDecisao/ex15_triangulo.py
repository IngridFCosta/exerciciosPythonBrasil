"""15-Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
A=float(input('Informa a medida do primeiro lado: '))
B=float(input('Informa a medida do segundo lado: '))
C=float(input('Informa a medida do terceiro lado: '))
somaAb=A+B
somaAc=A+C
somaBc=B+C
if somaAb > C or somaAc > B or somaBc >A:
    if A==B and A==C and B==C:
        print('Triangulo equilatero')
    elif A==B or A==C or B==C:
        print('Triangulo isósceles')
    elif A!=B and A!=C and B!=C:
        print('Triangulo escaleno')
else:
    print('Não forma um triangulo')
