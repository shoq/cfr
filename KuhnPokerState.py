class KuhnPokerState:
	def __init__(self, cards = None, history = ""):
		self.cards = cards
		self.history = history
		
	def nextHistory(self, action):
		nextStep = ["p", "b"][action]
		newState = KuhnPokerState(self.cards, self.history + nextStep)
		return newState
		
	def copy(self):
		newState = KuhnPokerState(self.cards, self.history)
		return newState
		