"""28-O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de
carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre
o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.
"""
print('-'*10, 'Tipos de carne', '-'*10)
print('1- File Duplo\n'
      '2-Alcatra\n'
      '3- Picanha\n')
tipoCarne=int(input('Escolha o tipo de carne que deseja comprar: '))
qtdCarne=float(input('Escolha a quantidade de carne que deseja comprar: '))
print('-'*10, 'Tipo de pagamento', '-'*10)
print('1- Cartão Tabajara\n'
      '2- Á vista\n')
pagamento=int(input('Escolha o tipo de pagamento: '))

if tipoCarne==1:
    nome='Filé duplo'
    if qtdCarne <=5.00:
        preço=qtdCarne*4.90
    else:
        preço=qtdCarne*5.80
elif tipoCarne==2:
    nome='Alcatra'
    if qtdCarne<=5.00:
        preço=qtdCarne*5.90
    else:
        preço=qtdCarne*6.80
elif tipoCarne==3:
    nome='Picanha'
    if qtdCarne<=5.00:
        preço=qtdCarne*6.90
    else:
        preço=qtdCarne*7.80

if pagamento==1:
    pag='Cartao Tabajara'
    desconto=(preço*5)/100
    totCompra=preço-desconto
else:
    pag='Dinheiro á vista'
    desconto=0
    totCompra=preço

print('-'*10,'Hipermercado Tabajara','-'*10)
print('Recibo')
print(f'Tipo de carne {nome:->30}')
print(f'Quantidade (kg) {qtdCarne:->30}')
print(f'Tipo de pagamento {pag:->30}')
print(f'Preço total R$: {preço:->30}')
print(f'Descontos R$: {desconto:->30}')
print(f'Valor a pagar R$: {totCompra:->30}')