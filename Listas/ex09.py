A=[]
somaQ=[]
for x in range(1,11):
  A.append(int(input(f'Informe o {x}º número: ')))

for cont in A:
    q=cont*cont
    somaQ.append(q)

print(f'Lista dos números: {A} ')
print(f'Lista dos quadrados: {somaQ}')
print(f'A soma dos quadrados é: {sum(somaQ)}')
