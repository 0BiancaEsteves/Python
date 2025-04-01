from random import randint
from time import sleep
computador = randint (0, 5) #Faz o PC 'pensar'#
print('Vou pensar em um numero de 0 a 5. Tente adivinhar')
jogador = int(input('Em que numero eu pensei?: ')) #jogador tenta adivinhar#
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens você acertou')
else :   
    print('GANHEI! Eu pensei em {} número, você falou {}'.format(computador, jogador))
