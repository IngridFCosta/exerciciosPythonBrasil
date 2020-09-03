"""26-Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

print('-'*10, 'Posto de gasolina', '-'*10)
print('A- Álcool         preço R$: 2,50\n'
      'G-Gasolina        preço R$:1,90 ')

totLitros=float(input('Informe o total de litros vendidos: '))
tipoCombustivel=str(input('Informe o tipo de combustível: ')).upper().strip()

if tipoCombustivel=='A':
    if totLitros <=20:
       preço=totLitros*1.90
       desconto=(preço*3)/100
       preçoFinal=preço-desconto
       print(f'O preço a ser pago por {totLitros} litros de álcool é {preçoFinal:.2f} ')

    if totLitros > 20:
        preço=totLitros*1.90
        desconto=(preço*5)/100
        preçoFinal=preço-desconto
        print(f'O preço a ser pago por {totLitros} litros de álcool é {preçoFinal:.2f} ')
if tipoCombustivel=='G':
    if totLitros <=20:
        preço=totLitros*2.50
        desconto=(preço*4)/100
        preçoFinal=preço-desconto
        print(f'O preço a ser pago por {totLitros} litros de gasolina é {preçoFinal:.2f} ')
    if totLitros > 20:
        preço=totLitros*2.50
        desconto=(preço*6)/100
        preçoFinal=preço-desconto
        print(f'O preço a ser pago por {totLitros} litros de gasolina é {preçoFinal:.2f} ')

