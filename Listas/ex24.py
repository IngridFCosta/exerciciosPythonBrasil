import random
resultados=[]
for x in range(10):
    dados=random.randint(1,7)
    resultados.append(dados)

for i in range(6):
    print(f' O numero {i+1} saiu {resultados.count(i+1)} vezes')

print(f'Lista de resultados {resultados}')
