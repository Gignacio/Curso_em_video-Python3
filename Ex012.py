'''
Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preco = float(input('Informe o preço do produto? R$'))
percent = preco * 0.05
print('O produto que custrava R${:.2f}, na promoção com o desconto de 5% vai custar R${:.2f}.'.format((preco),(preco-percent)))