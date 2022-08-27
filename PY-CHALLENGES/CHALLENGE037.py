numi = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numi, bin(numi)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numi, oct(numi)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numi, hex(numi)))
else:
    print('Opção inválida. Tente novamente.')