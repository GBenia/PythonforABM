# A Distribuidora seta o preço inicial (randomico)
# Os postos tem que ter volume e preço inicial (inicial é randomico?)
# Consumidores tem que ter quantidade de tanque cheio inicial (fazer na classe)
import random


class Distribuidores:
    def __init__(self):
        self.custo = random.randrange(0, 10)

    def altera_custo(self, param):
        self.custo *= param


class Consumidores:
    def __init__(self, i):
        self.id = i
        self.capacity = 30
        self.level_gas = random.randrange(3, 30)

    def check_gas(self):
        if self.level_gas <= 0.2 * self.capacity:
            print('Go to the gas station')
            return True
        else:
            print('Go ahead')
            return False

class Postos:
    def __init__(self, p):
        self.identity = p
        self.tanque = random.randrange(200, 1000)
        self.dist_cost = 0
        self.vizinhos = list()


    def comprar(self, custo):
        if self.tanque <= 200:
            self.tanque += 800
            self.dist_cost = custo

    def set_price(self):
        media = sum([i.preco for i in self.vizinhos]) / len(self.vizinhos)


if __name__ == '__main__':
    d = Distribuidores()
    c = Consumidores(1)
    p = Postos(2)
    c.check_gas()
    print(p.tanque, c.level_gas)
