listaPrestacao=[]
prestacao=True
diasAtraso=True
def valorPagamento(prestacao,diasAtraso):
    while prestacao!=0:
        prestacao=float(input('Digite a prestação: '))
        if prestacao==0:
            break
        else:
            listaPrestacao.append(prestacao)
            diasAtraso=float(input('Digite os dias em atraso:'))
            if diasAtraso==0:
                print(f'Valor cobrado: {prestacao}')
            elif diasAtraso > 0:
                multa=prestacao*3/100
                juros=(prestacao*(0.1/100))*diasAtraso
                tot=prestacao+multa+juros
                print(f'Valor cobrado: {tot}')

valorPagamento(prestacao,diasAtraso)
print(f'Quantidade de prestações pagas:{len(listaPrestacao)} ')
print(f'Valor das prestações: R$ {sum(listaPrestacao)}')

