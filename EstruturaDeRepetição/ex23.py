"""Numeros primos"""
totDivisao=0
num=int(input('Escreva um número qualquer: '))
for num in range(2,num):
    primo = True
    for i in range(2,num):
        if (num%i==0):
            primo = False
            totDivisao+=1
    if primo:
        print(num)
        totDivisao+=1
print("Número de divisões", totDivisao)
