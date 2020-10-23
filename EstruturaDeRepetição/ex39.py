cont =1
maior=menor=0
while cont < 11:
    numero=int(input('Informe o numero do aluno: '))
    altura=int(input('Informe a altura em centímetros: '))
    cont+=1
    if altura > maior:
        maior=altura
        numeroMaior=numero
    if altura < maior:
        menor=altura
        numeroMenor=numero
print(f'Aluno mais alto-> Número: {numeroMaior}, altura: {maior}cm')
print(f'Aluno mais baixo-> Número: {numeroMenor}, altura: {menor}cm')

