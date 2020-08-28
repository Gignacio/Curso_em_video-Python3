'''
Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
pn = float(input('Primeira nota do aluno'))
sn = float(input('Segunda nota do aluno'))
print('A média entre {} e {} é igual a {:.1f}'.format(pn, sn, ((pn+sn)/2)))