listaA=[]
listaB=[]
listaC=[]
listaD=[]
for x in range(1,11):
    listaA.append(int(input(f'Informe o {x}º número: ')))
for x in range(1,11):
   listaB.append(int(input(f'Informe o {x}º número: ')))

for x in range(1,11):
   listaC.append(int(input(f'Informe o {x}º número: ')))

cont=0
for x in range(10):
    listaD.append(listaA[cont])
    listaD.append(listaB[cont])
    listaD.append(listaC[cont])
    cont+=1

print(listaD)
