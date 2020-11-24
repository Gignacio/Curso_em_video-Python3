'''
Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
from  math import hypot
co = float(input("Qual o valor do Cateto Oposto? "))
ca = (float(input("Qual o valor do cateto adjacente? ")))

'''
hi = (co ** 2 + ca ** 2) ** (1/2) 
'''
hi = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))