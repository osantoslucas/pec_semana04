def idade():
    dia_atual = int(input('Que dia é hoje?'))
    mes_atual = int(input('De qual mês? '))
    ano_atual = int(input('De qual ano? '))
    dia_nasc = int(input('Que dia voce nasceu? '))
    mes_nasc = int(input('Em que mês vocÊ nasceu? '))
    ano_nasc = int(input('Em que ano você nasceu? '))
    idade_anos = ano_atual - ano_nasc
    idade_meses = mes_atual - mes_nasc
    idade_dias = dia_atual - dia_nasc
    if mes_atual < mes_nasc:
        idade_meses = mes_nasc - mes_atual
        if dia_atual < dia_nasc:
            idade_dias = dia_nasc - dia_atual
            print(f'Você tem {idade_anos} anos {idade_meses} meses e {idade_dias} dias de idade.')
        else:
            print(f'Você tem {idade_anos} anos {idade_meses} meses e {idade_dias} dias de idade')
    elif mes_atual > mes_nasc:
        if dia_atual < dia_nasc:
            idade_dias = dia_nasc - dia_atual
            print(f'Você tem {idade_anos} anos {idade_meses} meses e {idade_dias} dias de idade. ')
        else:
            print(f'Você tem {idade_anos} anos {idade_meses} meses e {idade_dias} dias de idade')
    else:
        print(f'Você tem {idade_anos} anos {idade_meses} meses e {idade_dias} dias de idade.')
idade()
