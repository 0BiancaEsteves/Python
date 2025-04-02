número = int(input('Me diga um numero: '))
resultado = número % 2
if resultado == 0:
    print('O número {} par'.format(número))
else:
    print('O número {} impar '.format(número))