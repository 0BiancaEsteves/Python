dias = int (input('Quantos dias ficou alugado?: '))
km = float(input('Quantos KM foram rodados?: '))
pago = (dias * 60) + (km * 0.15)
print ('O total  pagar é de R${:.2f}'.format(pago))
