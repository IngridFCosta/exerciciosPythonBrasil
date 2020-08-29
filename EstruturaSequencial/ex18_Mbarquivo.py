"""18-Faça um programa que peça o tamanho de um arquivo
para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este
link (em minutos)."""

tamArquivo=int(input('Escreva o tamanho do arquivo em MB: '))
velocidade=int(input('Escreva a velocidadde da internet Mbps: '))


tempo=tamArquivo*velocidade
tempoM=tempo/60
print(f'O tempo aproximado de download é de {tempoM:.0f} minutos')

