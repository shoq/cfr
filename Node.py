
class Node:

	def __init__(self, actions, infoSet = ""):
		self.infoSet = infoSet;
		self.actionCount = len(actions)
		self.clearStrategySum()
		self.regretSum = [0] * self.actionCount
		self.actions = actions;
	
	def getStrategy(self, realizationWeight):
		strategy = [0] * self.actionCount
		normalizingSum = 0
		for a in range(self.actionCount):
			strategy[a] = self.regretSum[a] if self.regretSum[a] > 0 else 0
			normalizingSum += strategy[a]

		for a in range(self.actionCount):
			if normalizingSum > 0:
				strategy[a] /= normalizingSum
			else:
				strategy[a] = 1.0 / self.actionCount
			self.strategySum[a] += realizationWeight * strategy[a]

		return strategy


	def getAverageStrategy(self):
		avgStrategy = [0] * self.actionCount
		normalizingSum = 0
		for a in range(self.actionCount):
			normalizingSum += self.strategySum[a];
		for a in range(self.actionCount):
			if normalizingSum > 0:
				avgStrategy[a] = self.strategySum[a] / normalizingSum
			else:
				avgStrategy[a] = 1.0 / self.actionCount

		return avgStrategy
		
	def getActionCount(self):
		return self.actionCount
		
	def clearStrategySum(self):
		self.strategySum = [0] * self.actionCount
