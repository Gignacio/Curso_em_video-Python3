'''
Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
print('A sua parade tem a dimensão de {}x{} e sua sua área é de {}m².'.format(l, a, (l*a)))
print('Para pintar essa parede, você precisará de {}l de tinta'.format((l*a)/2))
