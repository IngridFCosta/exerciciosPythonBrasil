mes_ext = ['janeiro', 'fevereiro', 'março','abril', 'maio','Junho','Julho',
           'Agosto','Setembro','Outubro','Novembro','Dezembro']

diasExtenso=['Um', ' dois','Três', 'Quatro', 'cinco', 'seis', 'sete', 'oito',' nove', 'Dez',
             'Onze', 'Doze', 'treze', 'catorze', 'quinze', 'deseseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
             'Vinte um','Vinte dois', 'Vinte tres', 'Vinte quatro', 'Vinte cinco', 'Vinte seis', 'Vinte sete',
             'Vinte oito', 'Vinte nove', 'Trinta', 'Trinta e um']

def converterData():
    data_numeros = input("Digite uma data no seguinte formato: [DD/MM/AA]: ")
    while data_numeros[2] != '/' and data_numeros[5] != '/' and len(data_numeros) != 10:
        print("[digitação incorreta]")
        data_numeros = str(input("Digite uma data no seguinte formato: [DD/MM/AA]: "))

    dia, mes, ano = data_numeros.split("/")
    print (f'Data: {diasExtenso[int(dia)-1]} / {mes_ext[int(mes)-1]} / {ano}')

converterData()