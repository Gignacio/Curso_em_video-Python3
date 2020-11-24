'''
Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos
quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle
PA = input("Informe o nome do primeiro aluno: ")
SA = input("Informe o nome do segundo aluno: ")
TA = input("Informe o nome do terceiro aluno: ")
QA = input("Informe o nome do quarto aluno: ")

lista = [PA, SA, TA, QA]
shuffle(lista)

print('A ordem de apresentação é:', lista)
