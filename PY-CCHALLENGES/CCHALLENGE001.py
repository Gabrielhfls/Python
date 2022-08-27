from time import sleep

planeta = str(input('Digite algum planeta: '))
peso = int(input('Quantos kilos tem o objeto? '))

if planeta == 'Terra':
    n = (peso * 9,807) # Terra tem exatamente 9,807 m/s² de Aceleração da Gravidade
    print('PROCESSANDO...')
    sleep(1)
    print('Seu objeto de {}kg com a gravidade do planeta {} tem {:.2f}kg'.format(peso, planeta, n))

if planeta == 'Venus':
    n = (peso * 8.87) # Venus tem exatamente 8,87 m/s² de Aceleração da Gravidade
    print('PROCESSANDO...')
    sleep(1)
    print('Seu objeto de {}kg com a gravidade do planeta {} tem {:.2f}kg'.format(peso, planeta, n))

if planeta == 'Mercurio':
    n = (peso * 3.7) # Mercurio tem exatamente 3,7 m/s² de Aceleração da Gravidade
    print('PROCESSANDO...')
    sleep(1)
    print('Seu objeto de {}kg com a gravidade do planeta {} tem {:.2f}kg'.format(peso, planeta, n))

if planeta == 'Marte':
    n = (peso * 3.771) # Marte tem exatamente 3,771 m/s² de Aceleração da Gravidade
    sleep(1)
    print('Seu objeto de {}kg com a gravidade do planeta {} tem {:.2f}kg'.format(peso, planeta, n))
