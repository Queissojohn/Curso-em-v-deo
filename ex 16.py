#Programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteira
from math import trunc
x = float(input('Digite um número: '))
print(f'A parte inteira de {x} é {trunc(x)}')