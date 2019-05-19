"""O modelo representea uma interação entre shops que vendem
    fun e agentes que compram fun. Agentes e shops tem uma Accont,
    onde os recursos para compra e venda de fun são depositados"""

# Construção dos agentes do modelo

import random

# Cada Account tem um saldo (balance) que inicia com zero
# Cada Account tem métodos específicos para depositar e sacar recursos e outro para fazer pagamentos
class Account:
    def __init__(self, i):
        self.registration = i
        self.balance = 0

    def deposito(self, valor):
        self.balance += valor

    def saque(self, valor):
        if self.balance < valor:
            return False
        else:
            self.balance -= valor
            return True

    def pagamento(self, valor):
        self.balance -= valor
        return True

# Cada shop tem uma account, uma capacidade (quant de agentes que podem ser atendidos),
# um estoque de fun e um cost (preço de venda)
# tem também um método para realizar a venda de fun
class Shop:
    def __init__(self, s):
        self.identity = s
        self.account = Account(s)
        self.capacity = random.randrange(1, 15)
        self.fun = random.randrange(1, 15)
        self.cost = random.randrange(2, 20)


    def venda(self, valor):
        if self.capacity > 0:
            self.capacity -= 1
            if self.fun >= valor:
                self.fun -= valor
                return valor
            else:
                return False
        else:
            return False

# Cada Agente tem uma conta e um estoque de fun que inicia com zero
# Os agentes têm métodos para conferir se tem saldo suficiente para comprar fun (checa_grana) e para receber a fun adquirida (get_fun)

class Agent:
    def __init__(self, a):
        self.id = a
        self.account = Account(a)
        self.fun = 0

    def checa_grana(self, valor):
        if self.account.balance > valor:
            return True
        else:
            return False

    def get_fun(self, valor):
        self.fun += valor


if __name__ == '__main__':
    print(type(Account))
    print(type(Shop))
    print(type(Agent))
    joao = Agent(1)
    mesbla = Shop(1)
    print(joao)
    print(mesbla)
    joao.account.deposito(500)
    joao.account.saque(200)
    print(joao.account.balance)
    print(mesbla.capacity, mesbla.fun, mesbla.cost)
    print(mesbla.capacity)
