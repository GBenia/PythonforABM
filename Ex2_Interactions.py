import random
from Ex2_Agentes import Shop, Agent

# A função criar cria listas de agents e shops
def criar(f, n):
    res = list()
    for j in range(n):
        res.append(f(j))
    return res

# a função salaries deposita valores nas contas dos agentes
def salaries(ag):
    for i in range(len(ag)):
       ag[i].account.deposito(random.randrange(10, 50))

# a função interact gera a interação entre agentes e shops processando a compra de fun
def interact(lst_ag, lst_shop):
    for a in range(len(lst_ag)):
        loja_vez = random.choice(lst_shop)
        if loja_vez.capacity > 0 and lst_ag[a].checa_grana(loja_vez.cost) is True:
            loja_vez.venda(1)
            lst_ag[a].get_fun(loja_vez.fun)
            loja_vez.account.deposito(lst_ag[a].account.pagamento(loja_vez.cost))
        else:
            return False

# a função main_func realiza as interações a partir das listas de agenres e shops criados
def main_func(x1, x2):
    lista_agentes = criar(Agent, x1)
    lista_shops = criar(Shop, x2)
    salaries(lista_agentes)
    interact(lista_agentes, lista_shops)
    return lista_agentes, lista_shops


if __name__ == '__main__':
    quant_agentes = 10
    quant_shops = 4
    a, s = main_func(quant_agentes, quant_shops)
    print(a)
    print(s)
    #print(medias(quant_agentes))
    #print(medias(quant_shops))


