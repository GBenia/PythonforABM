'''Questão 8. Dicionários. Dado o dicionário: d = {‘a’: 0}: faça programas que 8.1 acrescente um par
(chave, valor) {‘b’: 1}, ao dicionário; 8.2 verifique se a key ‘c’ está presente? 8.3
Concatene um dicionário a um outro dicionário: e = {z : 23}. Use o método ‘update’!'''

d = {'a': 0}
d['b'] = 1

# para testar se o programa identifica uma chave c incluída no dicionário basta tirar o # da linha abaixo
#d['c'] = 4

print(d)

if 'c' in d:
    print('O dicionario d possui a chave c')
else:
    print('O dicionario d não possui a chave c')

e = {'z': 23}
d.update(e)
print(d)


