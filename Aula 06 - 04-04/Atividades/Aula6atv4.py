print('Calcule o IMC')
h = float(input('Digite sua altura em metros: '))
sexo = input('Digite seu sexo: (M|F)')

if sexo == 'm' or sexo == 'M':
    peso = (72.7*h) - 58
else:
    peso = (62.1*h) - 44.7
print(f'Seu peso ideal é: {peso:.2f}')