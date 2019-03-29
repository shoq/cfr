from statistics import mean
import random

NUM_ACTIONS = 3
ROCK = 0
PAPER = 1
SCISSORS = 2

def nonNegatify(inputs):
	return [x if x > 0 else 0 for x in inputs]
	
def normalize(inputs):
	total = sum(inputs)
	if total > 0:
		return [x / total for x in inputs]
	else:
		return [1.0/len(inputs) for x in inputs]
	
def createStrategy(regrets):
	return normalize(nonNegatify(regrets))

def getAction(strategy):
		r = random.random()
		cumulativeProbability = 0
		for a in range(NUM_ACTIONS):
			cumulativeProbability = cumulativeProbability + strategy[a]
			if r < cumulativeProbability:
				return a
		return NUM_ACTIONS - 1
	
def getRegrets(played):
	if played == ROCK:
		return [1, 2, 0]
	elif played == PAPER:
		return [0, 1, 2]
	else: #SCISSORS
		return [2, 0, 1]
	
def play(playerRegrets, opponentRegrets):
	'''
	This code doesn't matter; actual action is not relevant, only potential outcomes are
		player = createStrategy(playerRegrets)
		l = getAction(player)
	'''
	opponent = createStrategy(opponentRegrets)
	r = getAction(opponent)
	regrets = getRegrets(r)
	playerRegrets = [sum(x) for x in zip(regrets, playerRegrets)]
	return playerRegrets

def train(lhs, rhs):
	for i in range(10**5):
		lhs = play(lhs, rhs)
		rhs = play(rhs, lhs)
	
	return [lhs, rhs]

print ("Start ")
regrets = [0.0] * NUM_ACTIONS 
regrets[0] = 100

oppRegrets = [0.0] * NUM_ACTIONS 
oppRegrets[1] = 100

finals = train(regrets, oppRegrets)
print(normalize(finals[0]))
print(normalize(finals[1]))

print ("End ")




print("Done");
