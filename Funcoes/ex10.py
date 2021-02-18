import random
def jogoCraps():
    resultado= random.randrange(2,13)
    return resultado
def verificarJogo(lancamento):
    if lancamento in [7,11]:
        print(f'Parabéns você tirou {lancamento}, é um natural e ganhou o jogo!!')
    elif lancamento in [2, 3, 12]:
        print(f'Você tirou {lancamento}')
        print('Deu craps! Você perdeu!!')
    else:
        print(f'Seu ponto foi {lancamento}')
        resultado1=lancamento
        lancamento02=True
        while resultado1 != lancamento02:
            lancamento02 = random.randrange(2, 13)
            if lancamento02 ==7:
                print(f'Deu {lancamento02} Você perdeu!!')
                break
            elif lancamento02 == resultado1:
                print(f'Deu {lancamento02} Parabéns voce ganhou!')
            else:
                print(f'Deu {lancamento02}. Ainda não foi dessa vez! Aguarda o novo lançamento')

lancamento=jogoCraps()
verificarJogo(lancamento)


