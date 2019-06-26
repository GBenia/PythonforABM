"""
Este módulo cria as classes de agentes que irão simular interações de
um mercado de varejo de combustíveis: Distribuidora, postos de combustivies e
consumidores
ESTE MODELO RODA A PARTIR DO MÓDULO FINAL_GENERALIZACAO
"""

import random

# A Distribuidora inicia com um preço inicia e tem
#métodos para alterção desse preço que será o custo do produto dos postos de gasolina

class Distribuidores:
    def __init__(self):
        self.custo = 2

    def altera_custo(self, param):
        self.custo *= (1+param)

    def get_custo(self):
        return self.custo

# Os consumidores têm uma capacidade de aramzenamento de combustível
# e inciam com uma quantidade randômica de gasolina

class Consumidores:
    def __init__(self, i):
        self.id = i
        self.capacity = 60
        self.level_gas = self.capacity * random.random()

# Consumidor atualiza seu nível de combustível após abastecer
    def set_level_gas(self):
        self.level_gas = 60

 # O consumidor anda e gasta gasolina
    def drive(self):
        self.level_gas -= 6

#Abastece até a capacidade
    def get_level_gas(self):
        return self.level_gas

# Checa o nível de gasolina no tanque
    def check_gas(self):
        if self.level_gas <= 0.2 * self.capacity:
            return True
        else:
            return False

# Os postos têm custo (preço da distribuidora), preço (randômico em torno de 3
# e estoque de combustível (randômico) definidos inicialmente

class Postos:
    def __init__(self, p):
        self.identity = p
        self.tanque = random.randrange(150, 300)
        self.dist_cost = 2
        self.vizinhos = list()
        self.preco_posto = random.random() / 10  + 3

# Métdo que verifica o nível de estoque para ver se há necessidade de comprar mais gasolina
    def check_estoque(self):
        if self.tanque <= 200:
            return True
        else:
            return False

# Função que atualiza o custo da gasolina a partir da mudança de preço da distribuidora
    def altera_custo(self, value):
        self.dist_cost = value

# Define para cada posto um volume de vendas diário (randômico)
    def venda_dia(self):
        self.tanque -= random.randint(100, 300)

# Reduz o estoque do posto quando ele vende gasolina
    def update_tanque(self, gas):
        self.tanque -= gas

# Adiciona os vizinhos de cada posto
    def add_vizinhos(self, viz):
        self.vizinhos.append(viz)

# Atualiza o estoque de gasolina para a capacidade máxima após a compra junto à distribuidora
    def set_tanque(self):
        self.tanque = 1000

# Posto autaliza o preço a partir da comparação com preços dos vizinhos e da alteração do custo
    def set_price(self):
        preco_vizinho = min([i.preco_posto for i in self.vizinhos])
        self.preco_posto = self.dist_cost * 1.5
        if self.preco_posto > 1.05 * preco_vizinho:
            self.preco_posto = preco_vizinho * (1 + (random.randrange(0, 5) / 100))


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
