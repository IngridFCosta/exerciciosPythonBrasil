paisA=80000
paisB=200000
totAno=0
while paisB > paisA:
    paisA+=paisA*0.03
    paisB+=paisB*0.015
    totAno+=1
print(f'Total de anos para população A igualar a B {totAno}')
