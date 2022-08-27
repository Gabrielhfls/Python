distância = float(input('Qual é a distância da sua vigem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância *0.50
else:
    preço = distância * 0.40
print('E o preço da sua passagem será de R${:.2f}'.format(preço))