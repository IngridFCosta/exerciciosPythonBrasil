"""Como eu tive dúvidas nessa questão o codigo foi baseaddo no codigo do
https://github.com/go4Mor4/Lista4_Python/blob/master/Lista4_16.py"""

salarios = [
    [200,299],[300,399],[400,499],
    [500,599],[600,699], [700,799],
    [800,899],[900,999]
]
valSalario=0
vendas=True
listaQtd=[0,0,0,0,0,0,0,0,0]
while vendas!=0:
    vendas=float(input('Informe o valor da venda: '))
    if vendas==0:
        break
    else:
        valSalario=(vendas*0.9)+200
        if valSalario < 1000:
            for i in range(len(salarios)):
                if valSalario > salarios[i][0] and valSalario < salarios[i][1]:
                    listaQtd[i]+=1
        else:
            listaQtd[8]+=1
for i in range(len(salarios)):
    print(f'Entre R$ {salarios[i][0]} e R$ {salarios[i][1]}-{listaQtd[i]} '
          f'')
print(f'Salarios maiores que R$1000: {listaQtd[8]}')


