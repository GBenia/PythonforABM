import os
import statistics
from Final_Interacao import main_func
from Final_Agentes import Distribuidores


if __name__ == '__main__':
    p = []
    c = []
    d = Distribuidores()


    filename = 'precos_medios.csv'

    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'a') as f:
        f.write('Dia; Media Precos; Desvio_padrao; Coeficiente_variacao\n')
        postos, consumidores, distribuidor = main_func(p, c, d)
        print(precos)
        print(sum(precos) / len(precos))
        print(loja.vizinhos)
        print(distribuidor.custo)
        #preco_medio = statistics.mean(a.preco_posto in range(postos))
        #desvio_preco = statistics.stdev(postos.preco_posto)
        #cv_preco = desvio_preco / preco_medio
        #print(agentlist[i], shoplist[i], avg_fun, avg_agent_balance, avg_shop_balance, avg_cost)
        #f.write('{}; {:.2f}; {:.2f}; {:.2f}'.format(i,  preco_medio, desvio_preco, cv_preco))
        f.write('\n')




## obter preços diários de cada posto e da distribuidora
## calcular média, desvio padrao e coeficinte de variação dários
## gerar relatórios
