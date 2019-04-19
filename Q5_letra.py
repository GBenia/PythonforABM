# -*- coding: utf-8 -*-
"""
5. Escreva um programa que recebe uma letra e identifica se ela é vogal ou consoante.
"""

def t_str(x):
    if x in 'aeiou':
        print('A letra é uma vogal')
    else:
        print("A letra é uma consoante")


if __name__ == '__main__':
    let = str(input('Entre com uma letra:'))
    t_str(let)
    
