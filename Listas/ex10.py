listaA=[]
listaB=[]
listaC=[]
for x in range(1,11):
    numeroA=int(input(f'Informe o {x}º número: '))
    listaA.append(numeroA)
for x in range(1,11):
    numeroB=int(input(f'Informe o {x}º número: '))
    listaB.append(numeroB)
cont=0
for x in range(10):
    listaC.append(listaA[cont])
    listaC.append(listaB[cont])
    cont+=1

print(listaC)
