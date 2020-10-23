listaSaltos=[]
nome=str(input('Informe o nome do atleta: '))
if nome =='':
    print('Encerrando...')
    exit()
else:
    for cont in range(1,6):
        saltos=float(input(f'{cont}º salto: '))
        listaSaltos.append(saltos)

soma=sum(listaSaltos)-max(listaSaltos)-min(listaSaltos)
media=soma/3
print(f'Melhor salto: {max(listaSaltos)}')
print(f'Pior salto {min(listaSaltos)}')
print(f'A média dos demais saltos:{media:.2f} ')
print('-'*10,'Resultado final','-'*10)
print(f'{nome} : {media:.2f}')