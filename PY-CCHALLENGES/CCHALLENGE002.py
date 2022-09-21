from time import sleep
print('-=-=-'*8)
print('Calculadora de Aceleração.')
print('-=-=-'*8)

f = int(input('Qual força voce esta colocando no objeto? '))
ma = int(input('Seu primeiro objeto tem quanto de massa? '))
mb = int(input('Seu segundo objeto tem quanto de massa? '))
question = (input('Tem uma segunda força? '))

if question == 'sim' or question == 'tem' or question == 'yes':
    f1 = int(input('Qual a segunda força que voce esta colocando no objeto? '))
    fr = (f - f1)
    mr = (ma + mb)
    a = (fr / mr)
    print('CALCULANDO...')
    sleep(1.5)
    print('{} - {} = ({} + {}) x a'.format(f, f1, ma, mb))
    print('{} = {} x a'.format(fr, mr))
    print('a = {} / {} => a = {}m/s²'.format(fr, mr, a))

else:
    fr = (ma + mb)
    mr = (ma + mb)
    a = (f / fr)
    print('CALCULANDO...')
    sleep(1.5)
    print('{} = ({} + {}) x a'.format(f, ma, mb))
    print('{} = {} x a'.format(f, mr))
    print('a = {} / {} => a = {}m/s²'.format(f, mr, a))
