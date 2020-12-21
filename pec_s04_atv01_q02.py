dia1 = int(input('Dia: '))
mes1 = int(input('Mês: '))
ano1 = int(input('Ano: '))
data1 = dia1 + mes1 + ano1
dia2 = int(input('Dia: '))
mes2 = int(input('Mês: '))
ano2 = int(input('Ano: '))
data2 = dia2 + mes2 + ano2
if data1 > data2:
    print(f'{dia1}/{mes1}/{ano1} é mais recente que {dia2}/{mes2}/{ano2}.')
else:
    print(f'{dia2}/{mes2}/{ano2} é mais recente que {dia1}/{mes1}/{ano1}')
