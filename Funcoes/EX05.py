def somaImposto(taxaImposto,custo):
    percent=taxaImposto/100
    taxa=percent*custo
    totFinal=taxa+custo
    print(f' Preço final {totFinal}')

somaImposto(int(input('Informe o percentual do imposto: ')),
            float(input('Informe o custo do produto: ')))