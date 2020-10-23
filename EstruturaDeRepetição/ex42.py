totIntervalo25=totIntervalo50=totIntervalo75=totIntervalo100=0
numero=0
while numero >=0:
    numero=int(input('Informe um numero: '))
    if numero <0:
        break
    if numero>=0 and numero<=25:
        totIntervalo25+=1
    if numero > 25 and numero <=50:
        totIntervalo50+=1
    if numero >50 and numero <=75:
        totIntervalo75+=1
    if numero >75  and numero <=100:
        totIntervalo100+=1
print(f'Total de números no intervalo de 0 a 25: {totIntervalo25}')
print(f'Total de números no intervalo de 25 a 50: {totIntervalo50}')
print(f'Total de números no intervalo de 50 a 75: {totIntervalo75}')
print(f'Total de números no intervalo de 75 a 100: {totIntervalo100}')



