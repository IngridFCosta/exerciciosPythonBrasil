listaCarros=['Fusca   ','Gol     ', 'Onix    ', 'Punto   ', 'CrossFox']
listaKmLitro=[]
totLitros=[]
gasolinaP=2.25
for cont in range(5):
    print(f'Veiculo {cont+1}')
    print(f'Nome: {listaCarros[cont]}')
    listaKmLitro.append(float(input('Km por litro: ')))
print('Relatório final')
for x in range(5):
    print(f'{x+1}- {listaCarros[x]}', end="       ")
    print(f'{listaKmLitro[x]}', end="  ")
    print(f'{round(1000/listaKmLitro[x],2):.2f} litros', end="   ")
    print(f'R$ {round(1000/listaKmLitro[x],2)*gasolinaP:.2f}')