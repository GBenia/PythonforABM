# -*- coding: utf-8 -*-
"""Questão 1 - Escreva um programa que ache os números
divisíveis por 7 e por 13, entre o seu ano de
nascimento e 2701."""

print('Os números entre 1968 e 2701 divisíveis por 7 e 13 são:')

for i in range(1968, 2701):
    if (i % 7) == 0 and (i % 13) == 0:
        print(i)

