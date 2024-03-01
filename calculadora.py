from math import sqrt

while True:

    num1 = float(input('Insira o primeiro número: '))
    num2 = float(input('Insira o segundo número: '))

    print('Atualmente, temos disponível os operadores: \n+\n-\n*\n/\nPotência escreva: pow\nRaiz quadrada insira: //')

    operador = input('Qual operador você deseja utilizar? ')

    if operador == '+' or operador == 'Soma':
       soma = num1 + num2
       print('{} + {} = {}'.format(num1, num2, soma))
    elif operador == '-' or operador == 'Menos':
       menos = num1 - num2
       print('{} - {} = {}'.format(num1, num2, menos))
    elif operador == '*' or operador == 'x' or operador == 'Vezes':
        vezes = num1 * num2
        print('{} x {} = {}'.format(num1, num2, vezes))
    elif operador == '/' or operador == 'Dividir':
       divisao = num1 / num2
       print('{} / {} = {}'.format(num1, num2, divisao))
    elif operador == 'pow' or operador == '**' or operador == 'potência':
        potencia = pow(num1, num2)
        print('{} ** {} = {}'.format(num1, num2, potencia))
    elif operador == '//' or operador == 'Raiz quadrada':
        raiz = sqrt(num1, num2)
        print('{} // {} = {}'.format(num1, num2, raiz))
    else:
        print('Insira um operador válido')
    continuar = input('Deseja continuar? (s/n) ').lower().strip()
    if continuar not in ['sim', 's']:
        break

#teste git