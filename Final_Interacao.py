from Final_Agentes import Distribuidores, Consumidores, Postos
import random

def create(f, n):
    res = list()
    for j in range(n):
        res.append(f(j))
    return res
    # Só ocorre uma vez
    # Criar 20 postos, os 1000 consumidores, e uma distribuidora

    # Retorna uma lista de agentes e postos e distribuidora
    pass
    return None, None, None


def vizinhanca(postos):
    for p in postos:
        p.vizinhos(random.choices(postos, k=4))


def main(postos, consum, distr):
    # -1. Os postos compram gasolina
    for posto in postos:
        posto.comprar(distr.custo)
    # 0. Os consumidores se locomovem (gasto de gasolina)
    # 1. Os postos decidem os preços
    # Coletar dados gerais e output
    pass


if __name__ == '__main__':
    # Listas
    lista_postos = create(Postos, 20)
    lista_consumidores = create(Consumidores, 1000)
    #vizinhos = vizinhanca(lista_postos)
    #print(lista_postos[2:10].tanque)


        #p, c, d = create()

   # main(p, c, d)