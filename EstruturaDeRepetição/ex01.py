nota=float(input('Escreva uma nota entre 0 e 10: '))
while nota < 0 or nota > 10:
    print('Nota inválida! Tente novamente')
    nota=float(input('Escreva uma nota entre 0 e 10: '))
    if nota >= 0 and nota<=10:
        print(f'A nota é {nota}')
        break