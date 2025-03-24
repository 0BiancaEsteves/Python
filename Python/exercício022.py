nome = str (input('Me diga seu nome completo: ')).strip()
print ('ANALISANDO...')
print ('Seu nome em maiúsculos é: {}'.format(nome.upper()))
print ('Seu nome em minúsculas é: {}'.format(nome.lower()))
print ('Seu nome tem ao todo: {} letras'.format(len(nome)- nome.count(' ')))
###print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))###
separa = nome.split()
print('Seu primeiro nome é {} é ele tem {} letras'.format(separa[0], len (separa[0])))