# A Distribuidora seta o preço inicial (randomico)
# Os postos tem que ter volume e preço inicial (inicial é randomico?)
# Consumidores tem que ter quantidade de tanque cheio inicial (fazer na classe)
import random


class Distribuidores:
    def __init__(self):
        self.custo = 2

    def altera_custo(self, param):
        self.custo *= (1+param)


class Consumidores:
    def __init__(self, i):
        self.id = i
        self.capacity = 60
        self.level_gas = self.capacity * random.random()

    def add_gas(self):
        #volume = 60 - self.level_gas
        self.level_gas += 60 - self.level_gas

    def drive(self):
        self.level_gas -= 6

    def check_gas(self):
        if self.level_gas <= 0.2 * self.capacity:
            print('Go to the gas station')
            return True
        else:
            print('Go ahead')
            return False

    #def bestprice(self):
        #self



class Postos:
    def __init__(self, p, vizinhos=3, preco=3):
        self.identity = p
        self.tanque = random.randrange(150, 300)
        self.dist_cost = 2
        self.vizinhos = vizinhos
        self.preco_posto = preco

    def check_estoque(self):
        if self.tanque <= 200:
            return True
        else:
            return False

    def venda_dia(self):
        self.tanque -= random.randint(100, 300)

    #def comprar(self, custo):
    #    if self.tanque <= 200:
    #        self.tanque += 1000 - self.tanque
    #        self.dist_cost = custo

    def add_vizinhos(self, viz):
        self.vizinhos = viz

    def set_price(self, postos):
        preco_vizinho = min([i.preco_posto for i in postos])
        self.preco_posto = self.dist_cost * 1.5
        if self.preco_posto > 1.05 * preco_vizinho:
            self.preco_posto = preco_vizinho * (1 + (random.randrange(0, 5) / 100))
        else:
            return preco_posto


if __name__ == '__main__':
    d = Distribuidores()
    c = Consumidores(200)
    p = Postos(25)
    d.altera_custo(0.5)
    c.check_gas()
    p.add_vizinhos(3)
    #p.set_price()
    p.check_estoque()
    print(p.tanque, c.level_gas, d.custo, p.vizinhos, p.venda_dia)
