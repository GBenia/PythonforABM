import random


class Distribuidores:
    def __init__(self, i):
        self.id = i
        self.custo = 2

    def altera_custo(self, param):
        self.custo *= (1+param)

class Postos:
    def __init__(self, p, preco=3, v=3, c=2):
        self.identity = p
        self.tanque = random.randint(150, 300)
        self.dist_cost = c
        self.vizinhos = v
        self.preco_posto = random.randint(2, 4)
        self.venda_dia = random.randint(150, 300)

    def add_vizinhos(self, viz):
        self.vizinhos = viz

    def check_estoque(self):
        if self.tanque <= 200:
            return True
        else:
            return False

    def set_price(self):
        #preco_vizinho = min([i.preco_posto for i in lojas])
        self.preco_posto = self.dist_cost * 1.5
        if self.preco_posto > 1.05 * preco_vizinho:
            self.preco_posto = preco_vizinho * (1 + (random.randrange(0, 5) / 100))
        else:
            return preco_posto

if __name__ == '__main__':
    d = Distribuidores(1)
    p = Postos(15)
    if p.check_estoque is True:
        print("T")
    else:
        print('F')
    print(d.custo)
    d.altera_custo(0.2)
    print(d.custo)
    print(p.preco_posto, p.tanque, p.venda_dia)
    #p.set_price()
    print(p.vizinhos)


