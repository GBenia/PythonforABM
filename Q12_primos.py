"""Questão 12. Escreva uma função que liste todos os números primos até 200.
    Utilize a divisão modular (%)."""

prime = []

for i in range(1, 200):
    count = 0
    for x in range(1, i+1):
        if i % x == 0:
            count += 1

    if count <= 2:
        prime.append(i)

print(prime)

