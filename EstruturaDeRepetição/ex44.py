print('-'*10,'CANDIDATOS', '-'*10)
print('1- Candidato 01\n'
      '2- Candidato 02\n'
      '3- Candidato 03\n'
      '4- Candidato 04\n'
      '5- Voto Nulo\n'
      '6- Voto em Branco\n'
      '0- Sair\n')
voto= True
totCandidato01=totCandidato02=totCandidato03=\
totCandidato04=totNulos=totBrancos=0
while voto !=0:
    voto=int(input('Informe seu voto: '))
    if voto==1:
        totCandidato01+=1
    if voto==2:
        totCandidato02+=1
    if voto==3:
        totCandidato03+=1
    if voto==4:
        totCandidato04+=1
    if voto==5:
        totNulos+=1
    if voto==6:
        totBrancos+=1
totalVotos=totCandidato01+totCandidato02+totCandidato03+\
     totCandidato04+totNulos+totBrancos
pctVotosBrancos=(totBrancos/totalVotos)*100
pctVotosNulos=(totNulos/totalVotos)*100
print(f'Total de votos candidato 1:{totCandidato01}')
print(f'Total de votos candidato 2:{totCandidato02}')
print(f'Total de votos candidato 3:{totCandidato03}')
print(f'Total de votos candidato 4:{totCandidato04}')
print(f'Total de votos nulos:{totNulos}')
print(f'Total de votos em branco:{totBrancos}')
print(f'Percentual de votos nulos: {pctVotosNulos} %')
print(f'Percentual de votos brancos: {pctVotosBrancos} %')







