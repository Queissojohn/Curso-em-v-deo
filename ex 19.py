#Um professor quer sortear um dos 4 alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
lista = [a,b,c,d]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}.')