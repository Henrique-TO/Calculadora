def calculadora():
    n1= int(input('numero 1: '))
    n2=int(input('numero 2: '))
    soma= n1+n2
    subtração= n1-n2
    multiplicação= n1*n2
    divisão= n1/n2

    escolha= input(f'escolha uma função')
    if escolha == '+':
        print(f'{n1} + {n2} = {soma}')
    elif escolha == '-':
        print(f'{n1} - {n2} = {subtração}')
    elif escolha == '*'or escolha == 'x':
        print (f'{n1} X {n2} = {multiplicação}')
    elif escolha == '/':
        print(f'{n1} / {n2} = {divisão}')
    else:
        print('ERROR')

calculadora()