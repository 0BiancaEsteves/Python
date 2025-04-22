Salário = float(input('Me diga seu Salário: '))
if Salário <= 1250:
    novo = Salário + (Salário * 15/100)
else:
    novo = Salário + (Salário * 10/100)
print ('Quem ganha R${}, passará a ganhar R${}'.format(Salário, novo))
