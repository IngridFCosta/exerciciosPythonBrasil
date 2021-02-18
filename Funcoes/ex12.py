import random
def embaralharPalavra(palavra):
   embaralha=list(palavra)
   random.shuffle(embaralha)
   embaralha="".join(embaralha)
   print(embaralha)


embaralharPalavra(str(input('Digite uma palavra: ')))
