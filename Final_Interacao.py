"""
Este módulo realiza as interaçõeas entre distribuidora, postos e
consumidores, modelados no módlo Final_Agentes
ESTE MODELO RODA A PARTIR DO MÓDULO FINAL_GENERALIZACAO
"""

from Final_Agentes import Distribuidores, Consumidores, Postos
import random
from collections import defaultdict

#Define o parâmetro de alteração do preço da distribuidora
param = (random.randrange(-10, 10)) / 100

#Cria listas de agentes do modelo (postos e consumidores)
def create(f, n):
    res = list()
    for j in range(n):
        res.append(f(j))
    return res

#Função que adiciona postos vizinhos a cada posto do modelo
def vizinhanca(postos):
    for p in postos:
        # Trocar para questão das áreas
        temp = random.sample(postos, k=4)
        for i in temp:
            p.add_vizinhos(i)
    return postos

#Fução que executa as interações entre os agentes
def main_func():
    # Cria distribuidora, postos e consumidores
    distribuidor = Distribuidores()
    lista_consumidores = create(Consumidores, 1000)
    lista_postos = create(Postos, 20)

    # Adiciona vizinhos
    lista_postos = vizinhanca(lista_postos)
    precos = defaultdict(list)

    # Roda as ações diárias dos agentes
    for d in range(30):

        #carros testam nível de combustivel
        #carros escolhem melhor preço e abastecem
        # Carros consomem
        for carro in lista_consumidores:
            if carro.check_gas() is True:
                candidatos = random.sample(lista_postos, k=3)
                posto_vez = min(candidatos, key=lambda x: x.preco_posto)
                posto_vez.update_tanque(60 - carro.get_level_gas())
                carro.set_level_gas()
            else:
                carro.drive()

        # Distribuidora altera preços a cada 2 dias
        if d % 2 == 0:
            distribuidor.altera_custo(param)

        for loja in lista_postos:

            # Posto decide se compra gasolina
            if loja.check_estoque() is True:
                loja.set_tanque()
                loja.altera_custo(distribuidor.get_custo())
                loja.set_price()

            #Preço de cada posto em cada dia é armazenado para cálculo das estatísticas
            precos[d].append(loja.preco_posto)
            #Posto reduz a quantidade vendida do seu estoque
            loja.venda_dia()
    return precos


if __name__ == '__main__':
    precos = main_func()


