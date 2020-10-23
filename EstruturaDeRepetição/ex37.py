
codigo=1
pesoMaior=pesoMenor=mediaPesos=somaPesos=totpeso=0
altMaior=altMenor=mediaAlturas=somaAltura=totAltura=0
codmaisBaixo=pesoMaisbaixo=codMaisMagro=alturaMagro=0
while codigo > 0:
        codigo=int(input('Escreva seu código:' ))
        if codigo==0:
            break
        else:
            peso=float(input('Escreva seu peso: '))
            somaPesos+=peso
            totpeso+=1
            altura=float(input('Escreva a sua altura: '))
            somaAltura+=altura
            totAltura+=1
            #Verificando o peso
            if peso > pesoMaior:
                pesoMaior=peso
                codMaisGordo=codigo
                alturaMaisGordo=altura
            if peso < pesoMaior:
                pesoMenor=peso
                codMaisMagro=codigo
                alturaMagro=altura
            #Verificando a altura
            if altura > altMaior:
               altMaior=altura
               codMaisAlto=codigo
               pesoMaisAlto=peso
            if altura < altMaior:
                altMenor=altura
                codmaisBaixo=codigo
                pesoMaisbaixo=peso
mediaAlturas=somaAltura/totAltura
mediaPesos=somaPesos/totpeso

print(f'Cliente mais alto: Código-> {codMaisAlto}, peso->{pesoMaisAlto}, altura->{altMaior}')
print(f'Cliente mais baixo: Código->{codmaisBaixo}, peso->{pesoMaisbaixo},altura->{altMenor}')
print(f'Cliente mais gordo: Código->{codMaisGordo}, peso->{pesoMaior},altura->{alturaMaisGordo}')
print(f'Cliente mais magro: Código->{codMaisMagro}, peso->{pesoMenor},altura->{alturaMagro}')
print(f'Média de pesos {mediaPesos:.2f}')
print(f'Média de alturas {mediaAlturas:.2f}')

