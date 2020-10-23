
maiorIndice=menorIndice=\
    totVeiculos=totAcidentes=totCidades=\
    mediaVeiculos=mediaAcidentes=0
codMaior=codmenor=0
for cont in range(0,5):
    codigo=int(input('Informe o código da cidade: '))
    numVeiculos=int(input('Informe o número total de veiculos de passeio: '))
    totVeiculos+=numVeiculos
    numAcidentes=int(input('Informe o número de acidentes com vítimas: '))
    totAcidentes+=numAcidentes
    if totVeiculos < 2000:
        totCidades+=1
        mediaAcidentes=totAcidentes/totCidades
    if cont==0:
        maiorIndice=menorIndice=numAcidentes
    if numAcidentes > maiorIndice:
            maiorIndice=numAcidentes
            codMaior=codigo
    elif numAcidentes < menorIndice:
            menorIndice=numAcidentes
            codmenor=codigo

mediaVeiculos=totVeiculos/5
print(f'O maior indice de acidentes é {maiorIndice} e pertence a cidade {codMaior}')
print(f'O menor indice de acidentes é {menorIndice} e pertence a cidade {codmenor}')
print(f'Média de veículos das 5 cidades->{mediaVeiculos:.2f}')
print(f'Média de acidentes nas cidades com menos de 2000 veiculos->{mediaAcidentes}')