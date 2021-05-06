nome = str(input("Informe o nome: "))
espaco = ""
espaco2=""
for letra in nome:
    espaco += letra
for i in range(len(nome)):
    espaco2 = espaco[0:len(nome) -i:]
    print(espaco2)