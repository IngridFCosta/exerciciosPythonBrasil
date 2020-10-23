numero=int(input('Informe um numero inteiro: '))
tot=0
for numero in range(2,numero):
    primo=0
    for x in range(2,numero):
        if numero%x==0:
            primo=1
    if primo==0:
     print(numero)



