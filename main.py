import random
from enum import IntEnum

class Options(IntEnum):
	Rock = 0
	Paper = 1
	Scissors = 2
	Spock = 3
	Lizard = 4

class NormalCPU:
	def makeChoice(self):
		choice = Options(random.randint(0, len(Options) - 1))
		return choice
	def getSelf(self):
		return self

class CopyCPU(NormalCPU):
	def __init__(self):
		self.prevChoice = -1

	def makeChoice(self):
		if (self.prevChoice != -1):
			return Options(self.prevChoice)
		else:
			return Options(random.randint(0, len(Options) - 1))

	def userLastOption(self, input):
		self.prevChoice = input


outcome_dict = {
	Options.Rock: [Options.Scissors, Options.Lizard],
	Options.Paper: [Options.Rock, Options.Spock],
	Options.Scissors: [Options.Paper, Options.Lizard],
	Options.Spock: [Options.Scissors, Options.Rock],
	Options.Lizard: [Options.Paper, Options.Spock]
}

def getIntInput(prompt):
	choice = input(prompt)
	try:
		choice = int(choice)
		return choice
	except:
		print("Enter an integer!")
		getIntInput(prompt)

def chooseCPU():
	choice = getIntInput("Enter 1 for normal CPU, 2 for CPU that copies you: ")
	generateCPU(choice)

def generateCPU(choice):
	if (choice == 1): opponent = NormalCPU()
	else: opponent = CopyCPU()
	return opponent

def playGame():
	#generate CPU
	choice = getIntInput("Enter 1 for normal CPU, 2 for CPU that copies you: ")
	if choice == 1: cpu = NormalCPU()
	else: cpu = CopyCPU()
	
	#start game
	replay = True
	while replay:
		#display options
		for option in Options:
			print(f"{option.name}: {option.value}")

		#get player choice
		validChoice = False
		while (validChoice == False):
			choice = getIntInput("Enter one of the above options: ")
			if (choice in range(0,5)): validChoice = True

		#cpu makes choice and CopyCPU is updated
		cpuChoice = cpu.makeChoice()
		if (isinstance(cpu,CopyCPU)): cpu.userLastOption(choice)

		#calculate outcome of game
		print(f"You chose {Options(choice).name}, CPU chose {Options(cpuChoice).name}!")
		computeWinner(choice, cpuChoice)

		#check if user wants to replay
		userReplay = input("Enter y or Y to replay, anything else to quit: ")
		if userReplay not in ["y", "Y"]: replay = False

def computeWinner(userChoice, cpuChoice):
	if userChoice == cpuChoice: print("Tie!")
	elif cpuChoice in outcome_dict[userChoice]: print("You Win!")
	else: print("You Lose!")
	
if __name__ == "__main__":
	playGame()