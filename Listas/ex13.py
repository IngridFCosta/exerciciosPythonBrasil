meses=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'
       'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas=[]
mediaAnual=0
cont=0
for x in range(1,5):
    temperaturas.append(float(input(f'Informe a temperatura do mês de {[meses[cont]]}: ')))
    cont+=1
    mediaAnual=sum(temperaturas)/len(temperaturas)
print(f'Média anual das temperaturas: {mediaAnual}°')

print('Meses com temperatura acima da média')
for x in range(4):
    if temperaturas[x] > mediaAnual:
        print(f'Mês: {meses[x]}', end="-> ")
        print(f'Temperatura: {temperaturas[x]}°')
