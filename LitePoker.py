from LitePokerState import LitePokerState
from Node import Node
import random

class LitePoker:
	
	CardTranslations = { 2: "2", 3: "3", 4: "4", 5:"5",6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11: "J", 12: "Q", 13: "K", 14: "A" }
	
	def isTerminal(self, gameState):
		history = gameState.history
		return len(history) > 1 and (history[-1] == 'p' or history[-2:] == "bb")
		
	def getOutcome(self, gameState, player, opponent):					
		lastActions = gameState.history[-2:]
		if lastActions == 'pp':
			isPlayerCardHigher = gameState.cards[player] > gameState.cards[opponent]
			return 1 if isPlayerCardHigher else -1
		elif lastActions == 'bp':
			return 1
		elif lastActions == 'bb':
			isPlayerCardHigher = gameState.cards[player] > gameState.cards[opponent]
			return 2 if isPlayerCardHigher else -2
	
	def applyGameEvents(self, gameState):
		if len(gameState.history) == 0:
			newState = gameState.copy()
			newState.cards = self.drawCards()
			return newState
		else:
			return gameState
	
	def drawCards(self):
		cards = list(LitePoker.CardTranslations.keys())
		c1 = random.choice(cards)
		leftCards = list(filter(lambda x: x != c1, cards))
		c2 = random.choice(leftCards)
		return [c1,c2]
		
	def createState(self):
		return LitePokerState()
		
	def createNode(self, infoSet):
		return Node(2, infoSet)
		
	def getInfoSet(self, gameState):
		player = self.getCurrentPlayer(gameState)
		return str(LitePoker.CardTranslations[gameState.cards[player]]) + gameState.history
		
	def getCurrentPlayer(self, gameState):
		plays = len(gameState.history)
		player = plays % 2
		return player
