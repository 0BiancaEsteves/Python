velocidade = float(input('Qual a velocidade do carro?: '))
if velocidade >80:
    print('Você esta multado! O limite é 80KM/h')
    multa = (velocidade - 80) * 7
    print('Sua multa é de: {}'.format(multa))
print('Tenha um bom dia, dirija em segurança!')