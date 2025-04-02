distancia = float(input('Qual é a distancia da sua viagem?: '))
print('Você está prestes a começar uma viagem de {}KM'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('É opreço da sua passagem será de R${:.2f}'.format(preço))