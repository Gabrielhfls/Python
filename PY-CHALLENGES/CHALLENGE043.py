peso = int(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso adequado!')

elif 18.5 <= imc < 24.9:
    print('Você está com o peso adequado!')

elif 24.9 <= imc < 29.9:
    print('Você está em SOBREPESO!')

elif 30 <= imc < 34.9:
    print('Você está na OBESIDADE GRAU I')

elif 35 <= imc < 39.9:
    print('Você está na OBESIDADE GRAU II ')

elif imc > 40:
    print('Você está em OBESIDADE GRAU III')