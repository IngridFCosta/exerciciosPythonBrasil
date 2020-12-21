
listaDefeitos=['Necessita de esfera             ', 'Necessita de limpeza            ',
          'Necessita troca do cabo/conector','Quebrado ou inutilizado         ']
numIdentificacao=[]
numID=True
numDefeito=0
defeitos=[]
while numID!=0:
    numID=int(input('Numero de identificação: '))
    if numID==0:
        break
    else:
        numDefeito=int(input('Informe o numero do defeito: '))
        defeitos.append(numDefeito)
        numIdentificacao.append(numID)

print(f'Total de Mouses: {len(numIdentificacao)}')
print('Situação', end=" "*32)
print('Defeitos', end=" "*10)
print('Porcentagem')

for x in range(len(listaDefeitos)):
    print(f'{x+1}-{listaDefeitos[x]}',end=" "*10)
    print(f'{defeitos.count(x+1)}', end=" "*15)
    print(round(100* defeitos.count(x+1)/len(numIdentificacao),2), "%")

