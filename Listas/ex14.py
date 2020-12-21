perguntas=['Telefonou para a vitima?', 'Esteve no local do crime?',
           'Mora perto da vitima','Devia para a vitima?',
           'Já trabalhou para a vitima?']
sim=[]
nao=[]
for x in range(0,5):
    resposta=str(input(f'Você {perguntas[x]}' )).upper().strip()
    if resposta=='SIM':
        sim.append(resposta)
    else:
        nao.append(resposta)
if len(sim)==2:
    print('Você é suspeito!')
elif len(sim)==3 or len(sim)==4:
    print('Você é cúmplicce')
elif len(sim)==5:
    print('Você é o assassino!')
else:
    print('Você é inocente!')
print('Caso encerrado!')