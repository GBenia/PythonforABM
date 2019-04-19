"""Questão 3. Altere o programa da questão 2 para que o que usuário
possa entrar com o número máximo de estrelas."""

maximo = int(input('Entre com o número máximo de estrelas:'))

# Número máximo é a quantidade de estrelas da linha maior, que fica no centro do desenho

for i in range(maximo + 1):
    print('*' * i)

for i in reversed(range(maximo)):
    print('*' * i)