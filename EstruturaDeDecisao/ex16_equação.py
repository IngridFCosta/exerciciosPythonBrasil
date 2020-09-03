"""16-Faça um programa que calcule as raízes de uma equação do segundo grau,
 na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
  as consistências, informando ao usuário nas seguintes situações:
-Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
e o programa não deve fazer pedir os demais valores, sendo encerrado;
-Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
-Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
-Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""
import  math
a=int(input('Escreva o valor de A: '))
if a == 0:
    print('A equação não é do segundo grau')
    exit()
else:
    b=int(input('Escreva o valor de B: '))
    c=int(input('Escreva o valor de C: '))

delta=(b*b)-4*a*c
if delta < 0:
    print(f'Valor do delta: {delta}')
    print('A equação não possui raizes reais')
    exit()
elif delta==0:
    print(f'A equação possui apenas uma raiz real:  {delta}')
else:
    x=math.sqrt(delta)
    x1=(-b+x)/2*a
    x2=(-b-x)/2*a
print(f'X1= {x1}')
print(f'X2= {x2}')



