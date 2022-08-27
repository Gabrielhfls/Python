from datetime import date

nasc = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = (atual - nasc)
c1 = (18 - idade)
c2 = (atual + c1)
c3 = (c1 + atual)
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(c1))
    print('Seu alistamento será em {}.'.format(c2))
elif idade > 18:
    c1 = (idade - 18)
    print('Você já deveria ter se alistado há {} anos.'.format(c1))
    print('Seu alistamento ja foi em {}.'.format(c3))
else:
    print('Você tem que se alistar IMEDIATAMENTE!!!')