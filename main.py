import random
import matplotlib.pyplot as plt
from cfr import cfr
import Node
from KuhnPoker import KuhnPoker
from CoinTossPlaySubgame import CoinTossPlaySubgame

PASS = 0
BET = 1

def train(nodes, iterations, **options):
	game = KuhnPoker()
	util = 0
	utilOverTime = []
	doPlot = options.get("doPlot") == True
	
	for i in range(iterations):
		gameState = game.createState()
		util += cfr(nodes, game, gameState, 1, 1)
		
		# plot
		if doPlot:
			utilOverTime.append(util / (i + 1) if i > 10000 else None)
		# countdown
		if i % (iterations / 100) == 0 and i > 0:
			print(f"{i / (iterations / 100)}%\r", end="")
	print("Average game value: ", util / iterations)
	
	if doPlot:
		plt.plot(utilOverTime)
		plt.plot([-0.05555555] * len(utilOverTime))
		plt.show()
		

nodeMap = {}
train(nodeMap, 1000) # Pretrain for the current strategy to converge a bit
for n in nodeMap.values():
	n.clearStrategySum()
train(nodeMap, 300000, doPlot = True)

print("Infoset\tPass\tBet")
results = list(nodeMap.values())
results.sort(key = lambda x: 
	0 if x.infoSet[0] == "J" else
	1 if x.infoSet[0] == "Q" else 2)


for n in results:
	l = list(enumerate(n.getAverageStrategy()))
	print(n.infoSet, '\t', list(map(lambda x: f'{n.actions[x[0]]}: {x[1]:0.4f}', l)))
	
# Check teorethical corectness for strategy values 
alpha = nodeMap["J"].getAverageStrategy()[BET]
print(f"Jack bet\t\t\t\t  {alpha:.4f}")

checks = [
	("King bet", "K", BET, alpha * 3),
	("Queen bet", "Q", BET, 0),
	("Queen call", "Qpb", BET, alpha + 1.0/3)
]

for check in checks:
	probability = nodeMap[check[1]].getAverageStrategy()[check[2]]
	print(f'{check[0]}\texpected: {check[3]:.4f}, actual: {probability:.4f}, diff: {abs(check[3] - probability):.4f}', 
		"OK" if abs(check[3] - probability) < 0.03 else "NOOO")

