# -*- coding: utf-8 -*-
"""
Questão 4 - Escreva um programa que corre os números de 1 a 50 e imprime. Mas, quando for múltiplo
de três, imprima ‘Oops’, quando for múltiplo de 5 imprima ‘Doo’, quando for de ambos
imprima ‘OopsDoo’.
"""

for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i, 'Oops')
    elif i % 5 == 0 and i % 3 != 0:
        print(i, 'Doo')
    elif i % 3 == 0 and i % 5 == 0:
        print(i, 'OopsDoo')
    else:
        print(i)

