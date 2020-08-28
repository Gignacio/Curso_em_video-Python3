"""
Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

"""

sal = float(input('Informe o seu salário? R$'))

percent = sal*0.15

print('Um funcionário que ganhava R${:.2f}, com o aumento de 15%, passa a receber R${:.2f}'.format(sal,(sal+percent)))