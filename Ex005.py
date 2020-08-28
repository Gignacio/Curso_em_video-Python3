'''
Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

a = int(input('Digite um número'))

print('Análisando o balot {}, o seu antecessor é {} e o seu sucessor é {}'.format(a, (a - 1), (a + 1)))
