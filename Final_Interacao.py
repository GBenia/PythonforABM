from Final_Agentes import Distribuidores, Consumidores, Postos
import random
import os
import statistics


param = (random.randrange(-10, 10)) / 100


def create(f, n):
    res = list()
    for j in range(n):
        res.append(f(j))
    return res


def vizinhanca(postos):
    for p in postos:
        # Trocar para questão das áreas
        p.add_vizinhos(random.choices(postos, k=4))


def main_func(postos, consum, distribuidor):
    #cria postos e consumidores
    #lista_consumidores = create(Consumidores, 10000)
    lista_postos = create(Postos, 20)
    precos = []
    # Adicionar vizinhos
    #vizinhanca(postos)
    # Rodar os dias

    for d in range(120):
        """
        #carros testma nível de combustivel
        #carros escolhem melhor preço e abastecem
        # Carros consomem

        for carro in consum:
            if carro.check_gas is True:
                posto_vez = min(random.choices(lista_postos, 3))
                posto_vez.tanque -= 60 - carro.level_gas
                carro.level_gas = 60
            else:
                carro.drive()
                """
        # Distribuidora altera preços a cada 7 dias
        if d % 7 == 0:
            distribuidor.altera_custo(param)
        # Posto decide se compara gasolina
        for loja in lista_postos:
            if loja.check_estoque is True:
                loja.tanque = 1000
                #loja.set_price()
                preco_vizinho = min([i.preco_posto for i in lista_postos])
                print(preco_vizinho)
                #loja.preco_posto = loja.dist_cost * 1.4
                if loja.preco_posto > 1.05 * preco_vizinho:
                    loja.preco_posto = preco_vizinho * (1 + (random.randrange(0, 5) / 100))
            precos.append(loja.preco_posto)
            loja.venda_dia()
            print(precos)
            print(sum(precos)/len(precos))
            #print(loja.vizinhos)
            print(distribuidor.custo)
            #print(preco_vizinho)
    return lista_postos, lista_consumidores, distribuidor

        #Obtém preços



        # Posto modifica preço?
        # Consumidor verifica se compra gasolina




if __name__ == '__main__':
    # Listas
    lista_postos = create(Postos, 20)
    lista_consumidores = create(Consumidores, 1000)
    o_distribuidor = Distribuidores()
    filename = 'precos_medios.csv'
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'a') as f:
        f.write('Dia; Media Precos; Desvio_padrao; Coeficiente_variacao\n')
    main_func(lista_postos, lista_consumidores, o_distribuidor)
    f.write('{:2f}'.format(sum(precos) / len(precos)))
    f.write('\n')
    print(o_distribuidor.custo)
    #print(lista_postos[preco_posto])

