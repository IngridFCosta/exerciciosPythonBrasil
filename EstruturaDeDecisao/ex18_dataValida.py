"""18-Faça um Programa que peça uma data
 no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

data = input("Digite a data no seguinte modelo: [11/07/2002] :")
if len(data) != 10:
    print("Não é uma data válida!")
else:
    if data[2] != '/' or data[5] != '/':
        print("Não é válida!")
    else:
        numeros_data = data.split('/')
        if int(numeros_data[0]) > 31:
            print("Não é uma data válida!")
        elif int(numeros_data[1]) > 12:
            print("Não é uma data válida")
        else:
            print(f"A data {data} é válida")