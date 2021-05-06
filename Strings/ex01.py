nome=str(input('Informe a primeira string: '))
nome2=str(input('Informe a segunda string: '))

def verificarStrings():
    print(f'Tamanho de {nome}: {len(nome)} caracteres')
    print(f'Tamanho de {nome2}: {len(nome2)} caracteres')
    if len(nome) == len(nome2):
        print('As strings tem o mesmo tamanho.')
    else:
        print('As strings tem tamanho diferente.')

    if nome!= nome2:
        print('As strings tem conteudo diferente.')
    else:
        print('As strings possuem conteúdos iguais')

verificarStrings()
