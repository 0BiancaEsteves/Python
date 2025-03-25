cidade = str (input('Em que cidade você nasceu? Se ela de iniciar com a palavra "Santo" falarei se é verdadeira?: ')).strip()
print(cidade[0:5].upper() == 'SANTO')