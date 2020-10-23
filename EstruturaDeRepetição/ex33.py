media=soma=tot=0
menor=maior=0
while True:
    temperatura=float(input('Informe a temperatura: '))
    soma+=temperatura
    tot+=1
    if tot==1:
        maaior=menor=temperatura
    if temperatura > maior:
        maior=temperatura
    elif temperatura < menor:
        menor=temperatura
    continuar=' '
    continuar=str(input('Deseja continuar? ')).upper().strip()
    while continuar not in 'SN':
        continuar=str(input('Deseja continuar? ')).upper().strip()
    if continuar=='N':
        break
media=soma/tot
print(f'Média de temperaturas:{media:.2f} graus')
print(f'A maior temperatura é {maior}°')
print(f'A menor temperatura é {menor}°')


