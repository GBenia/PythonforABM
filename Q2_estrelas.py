# -*- coding: utf-8 -*-
"""
Questão 2. Escreva um programa que imprima o seguinte padrão.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""


for i in range(10):
    print('*' * i)

for i in reversed(range(9)):
    print('*' * i)
