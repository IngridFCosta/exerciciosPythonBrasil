votos=[]
votosJogadores=[]
numeroJogadores=[]
voto=True
print('Quem foi o melhor jogador? ')
while voto!=0:
    voto=int(input('Número do Jogador (0=fim):'))
    if voto==0:
        break
    else:
        while voto > 23 or voto < 1:
            print('Informe um valor entre 1 e 23 ou 0 para sair')
            voto=int(input('Número do Jogador (0=fim):'))
        votos.append(voto)
print(f'Votos computados: {len(votos)}')

cont=1
for i in range(23):
    if cont not in votos:
        cont+=1
        continue
    else:
        votosJogadores.append(votos.count(cont))
        numeroJogadores.append(cont)
        print('Jogador', end="         ")
        print('Votos', end="         ")
        print('Percentual')
        print(cont, end="                  ")
        print(votos.count(cont), end="               ")
        print(round(100 * votos.count(cont) / len(votos), 2), "%")
        cont += 1

melhor =votosJogadores.index(max(votosJogadores))
print(f"O jogador mais votado foi o camisa  {numeroJogadores[melhor]} com {votosJogadores[melhor]} votos")
print(f'Ganhou com {round(100 * votosJogadores[melhor] / len(votos), 2)} % dos votos')


