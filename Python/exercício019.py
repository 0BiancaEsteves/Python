from random import choice
nome1 = str(input ('Me diga um nome que eu vou fazer um sorteio, primeiro nome: '))
nome2 = str(input('Outro nome: '))
nome3 = str(input('Outo nome: '))
nome4 = str (input('Outro nome: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))