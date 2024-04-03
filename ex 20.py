#O mesmo professor quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos 4 alunos e mostre a ordem ordenada
import random
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
lista = [a,b,c,d]
random.shuffle(lista)
print(f'A ordem da apresentacao será {lista}')