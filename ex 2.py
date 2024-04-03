dia = input('Digite o seu dia de nascimento: ')
mes = input('Digite o mês em que nasceu: ')
ano = input('Digite o ano que nasceu: ')
dia, mes, ano = [dia[0:2], mes[0:2], ano[0:4]]
print(f'Você nasceu no dia {dia}, mês {mes} do ano de {ano}')
