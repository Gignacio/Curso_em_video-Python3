'''
Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
c  = float(input("Informe a temperatura de °C "))

f = (c * (9/5)) + 32
print("A temperatura de {:.1f} correponde a {:.1f}F°".format(c,f))