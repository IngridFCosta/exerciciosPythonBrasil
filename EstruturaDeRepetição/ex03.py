nome=str(input('Informe seu nome: ')).upper().strip()
while len(nome)<=3:
    nome=str(input('Informe seu nome: '))

idade=int(input('Informe sua idade: '))
while idade < 0 or idade > 150:
    idade=int(input('Informe sua idade: '))

salario=float(input('Informe seu salário: '))
while salario==0:
    salario=float(input('Informe seu salário: '))

sexo=str(input('Informe seu sexo: (M/F)')).upper().strip()
while sexo not in 'MF':
    sexo=str(input('Informe seu sexo: (M/F)')).upper().strip()

estadoCivil=str(input('Informe seu estado civil: (c/s/v/d) '))
while estadoCivil not in 'csvd':
    estadoCivil=str(input('Informe seu estado civil: (c/s/v/d) '))

print('Dados validados com sucesso!')