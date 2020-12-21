listaSaltos=[]
while True:
    listaSaltos.clear()
    nome=" "
    nome=str(input('Informe o nome do Atleta: '))
    if nome== "":
        break
    for contador in range(1,4):
        listaSaltos.append(float(input(f'Informe o {contador}º salto:')))
    print('-'*10,'Resultado final','-'*10)
    print(f'Atleta: {nome}')
    print(f'Saltos: {listaSaltos}')
    print(f'Média dos saltos: {sum(listaSaltos) / len(listaSaltos):.2f}')
    print('-'*36)

