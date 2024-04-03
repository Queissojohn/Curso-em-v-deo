#Programa que leia um angulo qualquer e msotre na tela o valor do seno, ,cosseno e tangente desse angulo.
from math import sin,cos,tan,radians
a = int(input('Angulo: '))
print(f'''Seno de {a} = {sin(radians(a)):.2f}
Cosseno de {a} = {cos(radians(a)):.2f}
Tangente de {a} = {tan(radians(a)):.2f}''')