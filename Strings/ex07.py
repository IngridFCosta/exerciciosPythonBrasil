frase=str(input('Escreva uma frase: ')).upper()
espaco= frase.count(" ")
totVogais=[]
vogais=['A', 'E', 'I','O', 'U']
for i in range(len(frase)):
    if frase[i] in vogais:
        totVogais.append(frase[i])
print(f'Total de espaços: {espaco}')
print(f'Total de vogais: {len(totVogais)}')
print("A: ", totVogais.count('A'), "\nE: ", totVogais.count('E'), "\nI: ",
      totVogais.count('I'), "\nO: ", totVogais.count('O'), "\nU: ", totVogais.count('U'))

