lstCaracteres=[]
lstConsoantes=[]
for x in range(1,11):
    letras=str(input('Informe uma letra: ')).upper()
    if letras not in 'AEIOU':
        lstConsoantes.append(letras)
print(f'O total de consoantes é: {len(lstConsoantes)}')
print(f'Lista de consoantes: {lstConsoantes}')

