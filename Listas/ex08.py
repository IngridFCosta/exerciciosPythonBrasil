idade=[]
altura=[]
for x in range(1,6):
    idade.append((int(input(f'Informe a idade da {x}ª pessoa: '))))
    altura.append((float(input(f'Informe a altura da {x}ª pessoa: '))))
idade.sort(reverse=True)
altura.sort(reverse=True)
print(f'Lista de idades na ordem reversa: {idade}')
print(f'Lista de alturas na ordem reversa: {altura} ')