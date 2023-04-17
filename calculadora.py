n1 = 7
n2 = 15

operation = input('''
Por favor escolha a operação matematica que deseja realizar:
+ adição
- subtração
* multiplicação
/ divisão
''')

if operation == '+':
    print('{} + {} = '.format(n1, n2))
    print(n1 + n2)

elif operation == '-':
    print('{} - {} =  '.format(n1, n2))
    print(n1 - n2)

elif operation == '*':
    print('{} * {} =  '.format(n1, n2))
    print(n1 * n2)

elif operation == '/':
    print('{} / {} =  '.format(n1, n2))
    print(n1 / n2)

else:
    print('Por favor escolha uma operação valida.')
