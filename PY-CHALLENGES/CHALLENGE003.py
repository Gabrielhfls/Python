n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
cores = {'preto': '\033[1;30m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'magenta': '\033[1;35m',
         'cyan': '\033[1;36m',
         'cinzaclaro': '\033[1;37m',
         'cinzaescuro': '\033[1;90m',
         'vermelhoclaro': '\033[1;91m',
         'verdeclaro': '\033[1;92m',
         'amareloclaro': '\033[1;93m',
         'azulclaro': '\033[1;94m',
         'magentaclaro': '\033[1;95m',
         'cyanclaro': '\033[1;96m',
         'branco': '\033[1;97m',
         'pretofbranco': '\033[1;30;107m',
         'vermelhofcyanclaro': '\033[1;31;106m',
         'verdefmagentaclaro': '\033[1;32;105m',
         'amarelofazulclaro': '\033[1;33;104m',
         'azulfamareloclaro': '\033[1;34;103m',
         'magentafverdeclaro': '\033[1;35;102m',
         'cyanfvermelhoclaro': '\033[1;36;101m',
         'cinzaclarofcinzaescuro': '\033[1;37;100m',
         'cinzaescurofcinzaclaro': '\033[1;90;47m',
         'vermelhoclarofcyan': '\033[1;91;46m',
         'verdeclarofmagenta': '\033[1;92;45m',
         'amareloclarofazul': '\033[1;93;44m',
         'azulclarofamarelo': '\033[1;94;43m',
         'magentaclarofverde': '\033[1;95;42m',
         'cyanclarofvermelho': '\033[1;96;41m',
         'brancofpreto': '\033[1;97;40m'}
s = n1 + n2
print('A soma entre {}{} e {} vale {}'.format(cores['azulclarofamarelo'], n1, n2, s))
