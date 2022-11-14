import random

numero = random.randrange(0,6)
#print(numero)

chute = int(input('Digite um número entre 0 e 5: '))

if chute == numero:
    print('Você acertou!')
else:
    print('Você errou!')
