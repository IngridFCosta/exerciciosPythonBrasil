"""8-Faça um Programa que pergunte quanto você ganha por hora e o número
 de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

salHora=float(input('Informe quanto você ganha por hora: '))
horasT=float(input('Informe a quantidade de horas trabalhadas por mês: '))
salarioTotal=salHora*horasT
print(f'O salário total é : {salarioTotal:.2f}')