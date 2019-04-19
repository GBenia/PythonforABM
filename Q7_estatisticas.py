# -*- coding: utf-8 -*-
"""
Questão 7. Escreva um programa que, dada uma lista de números [2, 34, 5, 6, 5, 4, 32] qualquer,
retorne: o primeiro valor, o número de valores, o último valor, a soma, a média e a mediana.
Obs. Para listas com tamanho ímpar, a mediana é o valor do meio, quando ordenada
(sorted()). Para listas pares, os dois valores do meio.
"""

# como a mediana tem um cálculo mais complicado, fiz uma função específica para ela

def mediana(lista):
    lista.sort()
    return (lista[int((len(lista)-0.1)/2)] + lista[int(len(lista)/2)]) / 2


def stats(x):
    # lista = sort(x)
    print('A lista tem', len(x), 'elementos')
    print('A soma dos elementos da lista é', sum(x))
    print('O primeiro elemento da lista é', x[0])
    print('O último elemento da lista é', x[-1])
    print('A mediana dos elementos da lista é',(x[int((len(x)-0.1)/2)] + x[int(len(x)/2)]) / 2)


if __name__ == '__main__':
     listanum = [100, 4, 2, 6, 45, 8, 9, 11, 8, 10, 10, 45]
     stats(listanum)



