while True:

    altura = float(input('Poderia inserir a sua altura: '))
    peso = float(input('Poderia inserir o seu peso: '))

    calculo = peso / altura**2

    if calculo < 18.5:
        print('O seu IMC é {:.2f}, você está classificado como "Magreza"'.format(calculo))
    elif calculo <= 24.9:
        print('O seu IMC é {:.2f}, você está classificado como "Normal"'.format(calculo))
    elif calculo <= 29.9:
        print('O seu IMC é {:.2f}, você está classificado como "Sobrepeso", com obesidade grau I'.format(calculo))
    elif calculo <= 39.9:
        print('O seu IMC é {:.2f}, você está classificado como "Obesidade", com obesidade grau II'.format(calculo))
    else:
        print('O seu IMC é {:.2f}, você está classificado como "Obesidade", com obesidade grau III'.format(calculo))

    loop = input('Deseja continuar? (s/n) ').lower()
    print('-'*20)
    loopr = ['sim','s', 'yes']
    if loop not in loopr:
        break

        