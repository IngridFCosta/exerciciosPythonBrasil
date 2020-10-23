totPessoas=int(input('De quantas pessoas você quer verificar a idade? '))
cont=0
mediaIdade=0
soma=0
while cont < totPessoas:
    idade=int(input(f'Informe a idade da {cont+1}ª pessoa: '))
    cont+=1
    soma=idade+soma
mediaIdade=soma/totPessoas

print(f'Média de idade do grupo = {mediaIdade:.0f}')
if mediaIdade >=0 and mediaIdade <=25:
    print('Turma jovem')
elif mediaIdade > 25 and mediaIdade <=60:
    print('Turma adulta')
elif mediaIdade >60:
    print('Turma adulta')