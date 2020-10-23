numTermos= int(input('Quantos termos você quer mostrar? '))
t1=0
t2=1
cont=3
print('{} -> {}'.format(t1,t2), end='')
while cont <=numTermos:
    t3 = t1 + t2 #soma dos dois anteriores
    print('-> {}'.format(t3),end='')
    t1=t2 #mudança de posição
    t2=t3
    cont+=1
print('-> FIm')