"""Questão 9. Escreva uma função que faz um loop as keys de um dicionário.
    Se as keys forem vogais, eleve o valor ao quadrado. Caso contrário,
    set o valor para 0. Use if k in ‘aeiou’."""

letras = {'a': 4, 'b': 1, 'z': 23}
print(letras)

for k in letras.keys():
    if k in 'aeiou':
        letras[k] = letras[k] ** 2
    else:
        letras[k] = 0
print(letras)

        