salário = float(input('Qual o seu atual salário?:R$ '))
novo = salário + (salário * 15 / 100 )
print('Um funcionário que ganhava R${:.2f}, com o aumento de 15% vai ganhar R${:.2f}.'.format(salário, novo))
