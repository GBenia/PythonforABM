"""Questão 11. Escreva uma função que recebe uma lista e organiza os valores em keys e conta a frequência
de cada uma. Por exemplo: a lista [0, 0, 1, 1, 1, 2, 5], resultaria em: {1: 3, 0: 2, 2: 1, 5: 1}."""

# A função histogram faz um histograma com a frequencia de cada item da lista

def histogram(data):
    d = dict()
    for each in data:
        d[each] = d.get(each, 0) + 1
    return d


if __name__ == '__main__':
    b = [0, 0, 1, 1, 1, 2, 5]
    d1 = histogram(b)
    print(b)
    print(d1)
