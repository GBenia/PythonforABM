
import os

from Ex2_Interactions import main_func

# Este módulo realiza as interações entre shops e agents para diferentes  quantidades dessas classes
# Ao final gera relatório com as médias de fun, saldo (balance) e preços (cost)


if __name__ == '__main__':
    agentlist = [10, 50, 100, 500, 1000, 5000, 10000]
    shoplist = [5, 10, 15, 20, 25, 30, 35]

    filename = 'results.csv'

    if os.path.exists(filename):
        os.remove(filename)
    with open(filename, 'a') as f:
        f.write('No. Agents; No. Shops; Average Fun; Average Agent Account Balance; Average Shop Account Balance; Average Cost\n')
        for i in range(len(agentlist)):
            print(i)
            agents, shops = main_func(agentlist[i], shoplist[i])
            avg_fun = sum([a.fun for a in agents])/len(agents)
            avg_agent_balance = sum([a.account.balance for a in agents])/len(agents)
            avg_shop_balance = sum([s.account.balance for s in shops])/len(shops)
            avg_cost = sum([s.cost for s in shops])/len(shops)
            print(agentlist[i], shoplist[i], avg_fun, avg_agent_balance, avg_shop_balance, avg_cost)
            f.write('{}; {}; {:.2f}; {:.2f}; {:.2f}; {:.2f}'.format(agentlist[i], shoplist[i], avg_fun, avg_agent_balance, avg_shop_balance, avg_cost))
            f.write('\n')
