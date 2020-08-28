'''
Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
n1 = float(input('Digite um valor em metros: '))
print('{}km'.format(n1/1000))
print('{}hm'.format(n1/100))
print('{}dam'.format(n1/10))
print('{:.0f}dm'.format(n1*10))
print('{:.0f}cm'.format(n1*100))
print('{:.0f}mm'.format(n1*1000))