'''
Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
from random import choice
PA = input("Informe o nome do primeiro aluno: ")
SA = input("Informe o nome do segundo aluno: ")
TA = input("Informe o nome do terceiro aluno: ")
QA = input("Informe o nome do quarto aluno: ")

lista = [PA, SA, TA, QA]

sorteio = choice(lista)

print("O aluno sortiado foi: ",sorteio)