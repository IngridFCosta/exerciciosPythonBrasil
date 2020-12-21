listaVotos=[]
votosSistemas=[]
numeroSistemas=[]
sistemas=['W-Server   ', 'Unix       ', 'Linux      ', 'Netware    ', 'Mac OS     ', 'Outro      ']
voto=True

print('Qual o melhor sistema operacional para uso nos servidores?')
print('1- Windows Server\n'
      '2-Unix\n'
      '3-Linux\n'
      '4-Netware\n'
      '5-Mac OS\n'
      '6-Outro')
while voto!= 0:
    voto=int(input('Qual é o seu voto?'))
    if voto ==0:
        break
    else:
        while voto > 6 or voto < 1 or voto == " ":
            print('Informe um número entre o e 6:')
            voto=int(input('Qual é o seu voto?'))
        listaVotos.append(voto)

print('Sistema Operacional',end=" "*10)
print('Votos',end=" "*10)
print('Percentual')
print('-'*20 ,end="      ")
print('-'*10 ,end="      ")
print('-'*20)

contador=1

for pos in range(len(sistemas)):
    votosSistemas.append(listaVotos.count(contador))
    numeroSistemas.append(contador)
    print(f'{sistemas[pos]}', end=" "*20)
    print(listaVotos.count(contador), end=" "*20 )
    print(round(100 * listaVotos.count(contador) / len(listaVotos), 2), "%")
    contador += 1

print('Total', end=" "*26)
print(f'{len(listaVotos)}')
melhor =votosSistemas.index(max(votosSistemas))
indice_ganhador =votosSistemas.index(max(votosSistemas))
print(f"O Sistema operacional  mais votado foi o {sistemas[indice_ganhador].strip()} com {votosSistemas[melhor]} votos")
print(f'Ganhou com {round(100 * votosSistemas[melhor] / len(listaVotos), 2)} % dos votos')

