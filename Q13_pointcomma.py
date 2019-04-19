"""Questão 13. Escreva um programa que substitua ‘,’ por ‘.’ e ‘.’
por ‘,’ em uma string. Exemplo: 1,000.54 por 1.000,54."""


def subst(expression):
    express2 = ''
    for i in expression:
        if i == '.':
            express2 += ','
        elif i == ',':
            express2 += '.'
        else:
            express2 += i
    print(express2)


if __name__ == '__main__':
    expression = str(input('Entre com uma expressão qualquer:'))
    subst(expression)
