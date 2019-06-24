import random
from Simple_agentes import Distribuidores, Postos

param = (random.randrange(-10, 10)) / 100


def create(f, n):
    res = list()
    for j in range(n):
        res.append(f(j))
    return res


def vizinhanca(postos):
    for p in postos:
        p.vizinhos = create(Postos, 3)


if __name__ == '__main__':
    rede = create(Postos, 15)
    Dist = Distribuidores(1)
    Precos = list()
    for d in range(120):
        if d % 7 == 0:
            Dist.altera_custo(param)
        print(Dist.custo)
        for r in rede:
            preco_vizinho = min([i.preco_posto for i in rede])
            print(preco_vizinho)
            if r.check_estoque is True:
                r.tanque = 1000
                if r.preco_posto > 1.1 * preco_vizinho:
                    r.preco_posto = preco_vizinho * (1 + (random.randrange(0, 5) / 100))
                Precos.append(r.preco_posto)
                print(Precos)


    print(rede[1].dist_cost, rede[2].preco_posto, rede[2].vizinhos)
   # print(min(i.preco_posto for i in rede[1].vizinhos))
