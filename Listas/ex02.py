lista=[]
for x in range(1,5):
    numero=int(input(f'Informe o {x}º número: '))
    lista.append(numero)
lista.sort(reverse=True)
print(f'Lista em ordem inversa: {lista}')