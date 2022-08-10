from codecs import oem_decode
from string import octdigits


operation = input('''\nPor favor digite a operação matemática que você gostaria de completar 
+ para adição
- para subtração
* para multiplicação
/ para divisão\n\n Operação escolhida: ''')

number_1 = int(input('\nDigite o primeiro número: '))
number_2 = int(input('\nDigite o segundo número: '))

if(operation == '+'):
    print(f'\n{number_1} + {number_2} =', number_1 + number_2)
elif(operation == '-'):
    print(f'\n{number_1} - {number_2} =', number_1 - number_2)
elif(operation == '*'):
    print(f'\n{number_1} * {number_2} =', number_1 * number_2)
elif(operation == '/'):
    print(f'\n{number_1} / {number_2} =', number_1 / number_2)
else:
    print('\nVocê não digitou um operador válido, execute o programa novamente!')