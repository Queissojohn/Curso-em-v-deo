#média de duas notas
nome = input('Qual o seu nome completo? ')
nome = nome.title()
num1 = input('Escreva o valor da sua nota 1: ')
num2 = input('Escreva o valor da sua nota 2: ')
num1, num2 =[int(num1), int(num2)]
soma = num1 + num2
media = soma / 2
print(f'A média do aluno {nome} é: {media}')