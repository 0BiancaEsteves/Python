número = int(input('Me diga um numero qualquer: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print('ANALISANDO SEU NÚMERO {}'.format(número))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))