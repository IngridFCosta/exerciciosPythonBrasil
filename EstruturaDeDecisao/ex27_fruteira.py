"""27-Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
 e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente."""

qtdMorangos=float(input('Informe a quantidade de morangos (KG): '))
qtdMaças=float(input('Informe a quantidade de maçãs (KG): '))

if qtdMorangos<=5 and qtdMaças<=5:
    preçoMorango=2.50*qtdMorangos
    preçoMaça=1.80*qtdMaças
    totKG=qtdMorangos+qtdMaças
    preçoTotal=preçoMorango+preçoMaça
    if totKG > 8 and preçoTotal > 25.00:
        desconto=(preçoTotal*10)/100
        preçoFinal=preçoTotal-desconto
        print(f'O cliente terá que pagar R$: {preçoFinal:.2f}')
    else:
        print(f'O cliente terá que pagar R$: {preçoTotal:.2f}')

elif qtdMorangos > 5 and qtdMaças > 5:
    preçoMorango=2.20*qtdMorangos
    preçoMaça=1.50*qtdMaças
    totKG=qtdMorangos+qtdMaças
    preçoTotal=preçoMorango+preçoMaça
    if totKG > 8 and preçoTotal > 25.00:
        desconto=(preçoTotal*10)/100
        preçoFinal=preçoTotal-desconto
        print(f'O cliente terá que pagar R$: {preçoFinal:.2f}')
    else:
        print(f'O cliente terá que pagar R$: {preçoTotal:.2f}')