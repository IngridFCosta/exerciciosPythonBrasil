totNotas=float(input('Informe o total de notas que você quer calcular: '))
cont=0
media=soma=0
while cont < totNotas:
    nota=float(input(f'Informe a {cont+1}ª nota:'))
    cont+=1
    soma+=nota
media=soma/totNotas
print(f'A média é {media:.2f}')