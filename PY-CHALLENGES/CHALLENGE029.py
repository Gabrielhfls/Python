velc = float(input('Qual é a velocidade atual do carro? '))
limite = 80
if velc <=80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velc-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))