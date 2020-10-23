paisA=float(input('Informe a população inicial do pais A: '))
paisB=float(input('Informe a população inicial do pais B: '))
taxaA=float(input('Informe a taxa de crescimento do pais A: '))
taxaB=float(input('Informe a taxa de crescimento do pais B:'))
porcentA=taxaA/100
porcentB=taxaB/100
totAno=0

if paisA > paisB:
    while paisA > paisB:
        paisA+=paisA*porcentA
        paisB+=paisB*porcentB
        totAno+=1
    print(f'Total de anos para população A igualar a B {totAno}')
elif paisB> paisA:
    while paisB > paisA:
        paisA+=paisA*porcentA
        paisB+=paisB*porcentB
        totAno+=1
    print(f'Total de anos para população B igualar a A {totAno}')



