print('Especificação', end='       ')
print('Código', end='       ')
print('Preço')
print('Cachorro Quente', end='     ')
print('100', end='       ')
print('R$ 1,20')
print('Bauru Simples',end='       ')
print('101', end='       ')
print('R$ 1,30')
print('Bauru com ovo',end='       ')
print('102', end='       ')
print('R$ 1,50')
print('Hambúrguer',end='          ')
print('103', end='       ')
print('R$ 1,20')
print('Cheeseburguer',end='       ')
print('104', end='       ')
print('R$ 1,30')
print('Refrigerante',end='        ')
print('105', end='       ')
print('R$ 1,00')

totalPedido=0
codigo=True
preço=0
precoFinal=[]
while codigo > 0:
    codigo=int(input('Informe o código do pedido: '))
    if codigo==0:
        tot=sum(precoFinal)
        print(f'Preço total: {tot:.2f} R$')
        exit()
    quantidade=int(input('Informe a quantidade desejada: '))
    if codigo==100:
        preço=1.20
        preçoPedido=preço*quantidade
        precoFinal.append(preçoPedido)
    if codigo==101:
        preço=1.30
        preçoPedido=preço*quantidade
        precoFinal.append(preçoPedido)
    if codigo==102:
        preço=1.50
        preçoPedido=preço*quantidade
        precoFinal.append(preçoPedido)
    if codigo==103:
        preço=1.20
        preçoPedido=preço*quantidade
        precoFinal.append(preçoPedido)
    if codigo==104:
        preço=1.30
        preçoPedido=preço*quantidade
        precoFinal.append(preçoPedido)
    if codigo==105:
        preço=1.00
        preçoPedido=preço*quantidade
        precoFinal.append(preçoPedido)

