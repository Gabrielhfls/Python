from random import shuffle
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
al5= str(input('Quinto aluno: '))
lista = [al1, al2, al3, al4, al5]
shuffle(lista)
print('A ordem de apresentacao sera ')
print(lista)
