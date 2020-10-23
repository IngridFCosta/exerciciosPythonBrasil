while True:
    nome=str(input('Informe o nome de usuário: ')).upper().strip()
    senha=str(input('Informe sua senha')).upper().strip()
    if nome==senha:
        print('Erro! Usuário e senha não podem ser iguais!')
    else:
        print('Acesso confirmado!')
        break
