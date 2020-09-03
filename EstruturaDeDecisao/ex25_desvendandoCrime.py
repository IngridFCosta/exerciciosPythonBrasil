"""25-Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
 entre 3 e 4 como "Cúmplice"e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

pergunta1=str(input('Telefonou pra vitima? S/N ')).upper().strip()
pergunta2=str(input('Esteve no local do crime? S/N ')).upper().strip()
pergunta3=str(input('Mora perto da vitima? S/N ')).upper().strip()
pergunta4=str(input('Devia para a vitima? S/N ')).upper().strip()
pergunta5=str(input('Já trabalhou com a vítima? S/N ')).upper().strip()

lista=[pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
totSim=0
for resposta in lista:
    if resposta=='S':
        totSim+=1
if totSim==2:
    print('Suspeito')
elif totSim==3 or totSim==4:
    print('Cúmplice')
elif totSim==5:
    print('Assassino')
else:
    print('Inocente')
