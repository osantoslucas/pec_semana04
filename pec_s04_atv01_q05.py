
peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))

imc = peso/ (altura**2)

if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('PESO NORMAL.')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >=30 and imc < 35:
    print('OBESO LEVE')
elif imc >= 35 and imc < 40:
    print('OBESO MODERADO')
elif imc >= 40:
    print('OBESO MÓRBIDO')
print('FIM')
