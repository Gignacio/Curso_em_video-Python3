'''
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
'''
d = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar US${:.2f}'.format(d, (d*4.96)))
