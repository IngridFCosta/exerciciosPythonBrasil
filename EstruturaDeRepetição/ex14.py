totPares=0
totImpares=0
for x in range(1,11):
    numero=int(input(f'Informe o {x}º número: '))
    if numero%2==0:
        totPares+=1
    else:
        totImpares+=1
print(f'Total de números pares-> {totPares}')
print(f'Total de números ímpares-> {totImpares}')
