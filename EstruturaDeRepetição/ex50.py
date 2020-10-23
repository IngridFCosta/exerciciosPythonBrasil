termos=int(input('Quantos termos deseja mostrar? '))
cont=termos
numero1=1
numero2=1
soma01=soma02=0
print(f'H = {numero1} +', end=' ')
while cont > 0:
    numero2+=1
    print(f'{numero1}/{numero2}', end=' ')
    soma01+=numero1
    soma02+=numero2
    print(f' + ' if cont > 1 else'= ', end='')
    cont-=1
print(soma01, '/', soma02)


h = 1
n = 2
h_lista = []
n_lista = []
print("H = 1 +", end = "")
while n <= 10 -1:
    print(" ",h, "/", n, " + ", end="")
    h_lista.append(h)
    n_lista.append(n)
    n += 1

print(h, "/", n, " => ", sum(h_lista), "/", sum(n_lista), " => ", round(sum(h_lista) / sum(n_lista)), 2)

