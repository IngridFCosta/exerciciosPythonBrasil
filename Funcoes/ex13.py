altura=int(input('Informe a altura do retangulo: '))
largura=int(input('Informe a largura do retangulo: '))
while altura < 1 or altura > 20 or largura < 1 or largura > 20:
    print('Por favor, informe número dentro do intervalo [1 a 20]:')
    altura=int(input('Informe a altura do retangulo: '))
    largura=int(input('Informe a largura do retangulo: '))

def desenharTeto(largura):
    print("+", "  -  " * (largura - 2), "+")
def desenharParede(altura, largura):
    for i in range(altura - 2):
        print("|", "     " * (largura - 2), "|")

def desenharRetangulo(altura, largura):
    desenharTeto(largura)
    desenharParede(altura, largura)
    desenharTeto(largura)

desenharRetangulo(altura, largura)

