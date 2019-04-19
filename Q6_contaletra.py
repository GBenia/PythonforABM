# -*- coding: utf-8 -*-
"""
Questão 6. Escreva um programa que conte o número de letras de uma string.
"""

from string import ascii_letters

# A função con_let diferencia letras de outros caracteres

def con_let(x):
    symbol = []
    for i in x:
        if i not in ascii_letters:
            symbol += i
    print('O string tem', len(x), 'caracteres, dos quais', len(x) - len(symbol), 'são letras')
    
    
if __name__ == '__main__':
    frase = str(input('Entre com uma frase:'))
    con_let(frase)