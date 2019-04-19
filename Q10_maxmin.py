"""Questão 10. Escreva uma função que retorna os máximos e mínimos de um dicionário."""

db = {'a': 4, 'b': 1, 'z': 23, 'x': 34, 'e': 0}


minimo = db[min(db, key=db.get)]
print(minimo)
maximo = db[max(db, key=db.get)]
print(maximo)

