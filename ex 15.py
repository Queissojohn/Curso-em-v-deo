#Programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado
km = float(input('Distância percorrida: '))
dias = float(input('Quantidade de dias: '))
print(f'O valor total a ser pago é: R${(60 * dias) + (0.15 * km)}')

