def numeroReverso(numero):
    converter=str(numero)
    print(f'Número invertido: {converter[::-1]}')

numeroReverso(int(input('Informe um numero: ')))