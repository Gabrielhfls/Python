from datetime import date

nasc = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = (atual - nasc)

if idade <= 8:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação do atleta: PRÉ-MIRIM.')

elif idade <= 10:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação do atleta: MIRIM.')

elif idade <= 12:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação do atleta: PETIZ')

elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação do atleta: INFANTIL')

elif idade <= 16:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação do atleta: JUVENIL')

elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação do atleta: JUNIOR')

elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação do atleta: SENIOR')

elif idade > 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação do atleta: MASTER')