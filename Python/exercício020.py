from random import shuffle
nome1 = str(input('Me diga um nome, que irei embaralhar: '))
nome2 = str(input('Me diga outro nome: '))
nome3 = str(input('Outro nome: '))
nome4 = str(input('Outro nome: '))
lista = [nome1, nome2, nome3, nome4]
shuffle (lista)
print(' A ordem da apresentação do trabalho é')
print(lista)