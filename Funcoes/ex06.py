cont=True
def conversorHoras(hora24):
    hora12=hora24-12
    return hora12

def saidaHora(hora24,hora12, minuto):
    if hora24 >= 12 and hora24 <= 24:
        print(hora12,":", minuto, "PM")
    else:
        print(hora24, ":", minuto, "AM")

while cont !='N':
    hora24=int(input('Informe a hora: '))
    minuto=int(input('Informe os minutos: '))
    hora12=conversorHoras(hora24)
    saidaHora(hora24,hora12, minuto)
    cont=str(input('Deseja continuar? S/N: ')).upper().strip()
    if cont =='N':
        print('Fim do programa')
        break

