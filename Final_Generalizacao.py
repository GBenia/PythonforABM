"""
Este módulo roda as interações modeladas no módulo 'Final_Interacao
e calcula as médias dos precos dos postos em cada dia. Também são
calcualads medidas de dispersão (variância, desvio-padrão e coeficiente de
variação) para verificar se as interações entre os postos produzem uma tendência
de alinhamento dos preços dos combustíveis
"""

import os
import statistics
from Final_Interacao import main_func

if __name__ == '__main__':
    filename = 'precos_medios.csv'

    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'a') as f:
        f.write('Dia; Media Precos; Variância de precos; Desvio_padrao; Coeficiente_variacao\n')

        precos = main_func()
        for k in precos.keys():
            media = sum(precos[k]) / len(precos[k])
            varianca = statistics.variance(precos[k], media)
            desvio = statistics.stdev(precos[k], media)
            coef_variacao = desvio/media
            print('{}; {:.6f}; {:.6f}; {:.6f}; {:.6f}'.format(k, media, varianca, desvio, coef_variacao))
            f.write('{}; {:.6f}; {:.6f}; {:.6f}; {:.6f}'.format(k, media, varianca, desvio, coef_variacao))
            f.write('\n')

        #print(desvio)
## obter preços diários de cada posto e da distribuidora
## calcular média, desvio padrao e coeficinte de variação dários
## gerar relatórios
