print('Para encerrar o programa digite -1')
while True:
    total=0
    cont=0
    preço= True
    listaPreço=[]

    while preço > 0:
        preço=float(input(f'Produto {cont+1} R$:'))
        listaPreço.append(preço)
        total+=preço
        cont+=1
    if preço==-1:
        print('Encerrando o caixa...')
        break

    print(f'Total: {total:.2f}')
    dinheiro=float(input('Dinheiro R$:'))
    print(f'Dinheiro: {dinheiro:.2f}')
    print(f'Troco: {dinheiro-total:.2f}')
    print('Fim da Compra.Thank you,next...')


