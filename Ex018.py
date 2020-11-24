'''
Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
from math import radians, cos, sin, tan
ang = float(input("Informe um ângulo: "))

rad = radians(ang)

cos = cos(rad)
sen = sin(rad)
tan = tan(rad)

print("O ângulo de {} tem o Cosseno de {:.2f}".format(ang, cos))
print("O ângulo de {} tem o Seno de {:.2f}".format(ang, sen))
print("O ângulo de {} tem o Tangente de {:.2f}".format(ang, tan))