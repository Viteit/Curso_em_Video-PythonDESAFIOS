from random import randint
from time import sleep

numero = randint(0,5)
#print(numero)

chute = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)

if chute == numero:
    print('Você acertou!')
else:
    print('Você errou. Eu pensei no número {}!'.format(numero))
