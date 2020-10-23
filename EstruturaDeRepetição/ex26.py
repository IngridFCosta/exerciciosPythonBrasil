from time import sleep

totEleitor=int(input('Informe o total de eleitores: '))
print('-'*10,'Candidatos','-'*10)
print('Candidato 01-1\n'
      'Candidato 02-2\n'
      'Candidato 03-3')
cont=0
totVotos01=totVotos02=totVotos03=0
while cont < totEleitor:
    voto=int(input(f'Voto {cont+1}ª eleitor: '))
    cont+=1
    if voto==1:
        totVotos01+=1
    elif voto==2:
        totVotos02+=1
    elif voto==3:
        totVotos03+=1

print('-'*10,'Apuração','-'*10)
sleep(1)
print(f'Total de votos Candidato 01 {totVotos01}')
print(f'Total de votos Candidato 02 {totVotos02}')
print(f'Total de votos Candidato 03 {totVotos03}')