#Programa que leia o comprimento do cateto oposto e do catetos adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt,pow
c1 = float(input('cateto oposto: '))
c2 = float(input('cateto adjacente: '))
print(f'A hipotenusa vale {(sqrt(pow(c1,2) + pow(c2,2))):.2f}')

from math import hypot
c1 = float(input('cateto oposto: '))
c2 = float(input('cateto adjacente: '))
print(f'A hipotenusa vale {(hypot(c1,c2)):.2f}')