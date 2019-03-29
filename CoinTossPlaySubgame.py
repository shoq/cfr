from CoinTossPlaySubgameState import CoinTossPlaySubgameState
from Node import Node
import random

class CoinTossPlaySubgame:
	
	CardTranslations = { 1: "h", 2: "t" }
	Player0Actions = [ "optout", "play " ]
	Player1Actions = [ "heads ", "tails" ]
	
	def isTerminal(self, gameState):
		return (len(gameState.history) > 0 and gameState.history[-1] == 'o') or  len(gameState.history) > 1
		
	def getOutcome(self, gameState, player, opponent):					
		lastActions = gameState.history[-1]
		outcome = CoinTossPlaySubgame.CardTranslations[gameState.outcome]
		
		if lastActions == 'o':
			return 0 if outcome == 'h' else -0.5
		else:
			return -1 if lastActions == outcome else 1
	
	def applyGameEvents(self, gameState):
		if len(gameState.history) == 0:
			newState = gameState.copy()
			newState.outcome = self.toss()
			return newState
		else:
			return gameState
	
	def toss(self):
		faces = list(CoinTossPlaySubgame.CardTranslations.keys())
		outcome = random.choice(faces)
		return outcome
		
	def createState(self):
		return CoinTossPlaySubgameState()
		
	def createNode(self, gameState):
		infoSet = self.getInfoSet(gameState)
		if self.getCurrentPlayer(gameState) == 0:
			return Node(CoinTossPlaySubgame.Player0Actions, infoSet)
		else:
			return Node(CoinTossPlaySubgame.Player1Actions, infoSet)
		
	def getInfoSet(self, gameState):
		player = self.getCurrentPlayer(gameState)			
		outcome = "?" if player == 1 else str(CoinTossPlaySubgame.CardTranslations[gameState.outcome])
		return str(player) + "-" + outcome + "-" + gameState.history
		
	def getCurrentPlayer(self, gameState):
		plays = len(gameState.history)
		player = plays % 2
		return player
