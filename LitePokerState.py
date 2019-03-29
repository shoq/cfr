class LitePokerState:
	def __init__(self, cards = None, history = ""):
		self.cards = cards
		self.history = history
		
	def nextHistory(self, action):
		nextStep = ["p", "b"][action]
		newState = LitePokerState(self.cards, self.history + nextStep)
		return newState
		
	def copy(self):
		newState = LitePokerState(self.cards, self.history)
		return newState
		