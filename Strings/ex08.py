frase=str(input('Escreva uma frase: ')).replace(' ','')
fraseReversa=frase[::-1]
fraseReversa.strip()

print(fraseReversa)
if frase ==fraseReversa:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')